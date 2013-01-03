from ftpclient.statemachine import StateMachine, STATE_READY, STATE_CONNECTED, STATE_LOGGED
from ftpclient.directory_parser import parseListing
from ftpclient.filestream import FileStream

class Client:
	# interface of this class is more or less compatible
	# with org.apache.commons.net.ftp.FTPClient	
	
	# This interface does not provide additional error checking,
	# however provides warnings.
	
	def __init__(self, commandNet, dataNet):
		self.commandNet = commandNet
		self.dataNet = dataNet
		self.machine = StateMachine(commandNet)
		self.DATA_TRANSFER_CONFIRMATION_BUG = False
		self.PASV_RESPONSE_READ_BUG = False
	
	def setDataTransferConfirmationBug(self, value):
		self.DATA_TRANSFER_CONFIRMATION_BUG = value
	
	def setPasvResponseReadingBug(self, value):
		self.PASV_RESPONSE_READ_BUG = value
	
	def warn(self, message):
		print "WARN %s" % message

	def connect(self, host, port):
		if self.machine.getState() != STATE_READY:
			self.warn("Expecting STATE_READY")
		
		return self.machine.connect(host, port)
	
	def isConnected(self):
		return self.machine.getState() != STATE_READY

	def login(self, username, password):
		if self.machine.getState() != STATE_CONNECTED:
			self.warn("Expecting STATE_CONNECTED")
	
		suc = self.machine.user(username)
		if not suc:
			return False

		if self.machine.getState() == STATE_LOGGED:
			return True

		suc = self.machine.password(password)

		return suc

	def listFiles(self):
		if self.machine.getState() != STATE_LOGGED:
			self.warn("Expecting STATE_LOGGED")
	
		# todo: polish according to retrieveFile
		suc = self.machine.pasv()

		if not suc:
			return None

		dataSocket = self.machine.getDataSocket()
		
		## INJECTION
		# The transaction may go well (reponse code is OK) but the
		# returned IP address and port may not be readable.
		if not self.PASV_RESPONSE_READ_BUG:
			if dataSocket is None:
				self.machine.dataConnectionClearAfterError()
				return None
		else:
			self.warn("PASV_RESPONSE_READ_BUG is active")
		
		suc = self.dataNet.connect(dataSocket.hostname, dataSocket.port)
		
		if not suc:
			self.machine.dataConnectionClearAfterError()
			return None
		
		dataReader = self.dataNet.createNetworkReader()
		self.machine.dataConnectionEstablished()
		suc = self.machine.listing()
		if suc:
			data = dataReader.readAll()
			suc2 = self.machine.transferSuccessfullyDone()
			if not suc2:
				self.machine.dataConnectionClearAfterError()
				return None

			return parseListing(data)
		else:
			self.machine.dataConnectionClearAfterError()
			return None

	def changeWorkingDirectory(self, directory):
		if self.machine.getState() != STATE_LOGGED:
			self.warn("Expecting STATE_LOGGED")
			
		return self.machine.cwd(directory)
	
	def logout(self):
		if not self.isConnected():
			self.warn("Expecting isConnected")
			return False
			
		return self.machine.quit()
	
	def deleteFile(self, filename):
		if self.machine.getState() != STATE_LOGGED:
			self.warn("Expecting STATE_LOGGED")
			
		return self.machine.dele(filename)

	def retrieveFile(self, filename):
		if self.machine.getState() != STATE_LOGGED:
			self.warn("Expecting STATE_LOGGED")
			
		suc = self.machine.pasv()
		
		if not suc:
			return None
		
		dataSocket = self.machine.getDataSocket()
		
		## INJECTION
		# The transaction may go well (reponse code is OK) but the
		# returned IP address and port may not be readable.
		if not self.PASV_RESPONSE_READ_BUG:
			if dataSocket is None:
				self.machine.dataConnectionClearAfterError()
				return None
		else:
			self.warn("PASV_RESPONSE_READ_BUG is active")
					
		suc = self.dataNet.connect(dataSocket.hostname, dataSocket.port)
		
		if not suc:
			# This branch was added because of JPF, can not reproduce now.
			self.machine.dataConnectionClearAfterError()
			return None
		
		dataReader = self.dataNet.createNetworkReader()
		self.machine.dataConnectionEstablished()
		suc = self.machine.retr(filename)
		if suc:
			data = dataReader.readAll()
			suc2 = self.machine.transferSuccessfullyDone()
			## INJECTION: the fact that transferSuccessfullyDone may fail (because it reads
			# confirmation message) was discovered by JPF. Visible after two subsequent client.retrieveFile.
			if not self.DATA_TRANSFER_CONFIRMATION_BUG:
				if not suc2:
					# transaction failed, reset the state and return null
					self.machine.dataConnectionClearAfterError()
					return None
			else:
				self.warn("DATA_TRANSFER_CONFIRMATION_BUG is active")
			return data
		else:
			self.machine.dataConnectionClearAfterError()
			return None

	def retrieveFileStream(self, filename):
		if self.machine.getState() != STATE_LOGGED:
			self.warn("Expecting STATE_LOGGED")
			
		suc = self.machine.pasv()
		
		if not suc:
			return None
		
		dataSocket = self.machine.getDataSocket()

		## INJECTION
		# The transaction may go well (reponse code is OK) but the
		# returned IP address and port may not be readable.
		if not self.PASV_RESPONSE_READ_BUG:
			if dataSocket is None:
				self.machine.dataConnectionClearAfterError()
				return None
		else:
			self.warn("PASV_RESPONSE_READ_BUG is active")
		
		self.dataNet.connect(dataSocket.hostname, dataSocket.port)
		dataReader = self.dataNet.createNetworkReader()
		self.machine.dataConnectionEstablished()
		suc = self.machine.retr(filename)
		if suc:
			result = FileStream(dataReader, self.machine)
			result.setDATA_TRANSFER_CONFIRMATION_BUG(self.DATA_TRANSFER_CONFIRMATION_BUG)
			return result;
		else:
			self.machine.dataConnectionClearAfterError()
			return None
