
class StateException(Exception):
	def __init__(self, message):
		self.message = message

class Server:
	S_STATE_READY = 1;
	S_STATE_CONNECTED = 2;
	S_STATE_WAITING_PASSWORD = 21;
	S_STATE_LOGGED = 3;
	S_STATE_WAITING_DATA_CONNECTION = 4;
	S_STATE_DATA_CONNECTION_ESTABLISHED = 41;
	S_STATE_TRANSFERING = 5;

	S_STATE_LIST_TRANSFER_DONE = 51;
	S_STATE_FILE_TRANSFER_DONE = 52;
	
	ORDER_LISTING = "**LISTING**"
	
	STATE_STR = {
		1:"S_STATE_READY",
		2:"S_STATE_CONNECTED",
		21:"S_STATE_WAITING_PASSWORD",
		3:"S_STATE_LOGGED",
		4:"S_STATE_WAITING_DATA_CONNECTION",
		41:"S_STATE_DATA_CONNECTION_ESTABLISHED",
		5:"S_STATE_TRANSFERING",

		51:"S_STATE_LIST_TRANSFER_DONE",
		52:"S_STATE_FILE_TRANSFER_DONE",
	}
	

	def __init__(self):
		self.order = None
		self.state = self.S_STATE_READY
		self.command = None
		self.experimentErrorListing = False
	
	def assertState(self, shouldBe):
		if self.state != shouldBe:
			msg = "Server state is %s, should be %s." % (self.STATE_STR[self.state], self.STATE_STR[shouldBe])
			print msg
			raise StateException(msg)
	
	def setState(self, newState):
		#print "__state set ", self.STATE_STR[self.state], "=>", self.STATE_STR[newState]
		self.state = newState
	
	def isCmd(self, command, pattern):
		command = command.lower()
		pattern = pattern.lower()
		return command.startswith(pattern)
	
	def setExperimantErrorListing(self, value):
		self.experimentErrorListing = value
	
	def connectToCommand(self):
		self.assertState(self.S_STATE_READY)
		self.setState(self.S_STATE_CONNECTED)
		self.setCommand("GREETING")
	
	def connectToData(self):
		self.assertState(self.S_STATE_WAITING_DATA_CONNECTION)
		print "S:Connected on data port"
		self.setState(self.S_STATE_DATA_CONNECTION_ESTABLISHED)
	
	def reply(self):
		#cmd = self.command.strip()
		cmd = self.command # no stripping in rpython
		result = "500 UNDEF ERROR"
		
		try:
			if self.isCmd(cmd, "USER"):
				result = self.commandUser()
			elif self.isCmd(cmd, "GREETING"):
				result = self.greeting()
			elif self.isCmd(cmd, "PASV"):
				result = self.commandPasv()
			elif self.isCmd(cmd, "LIST"):
				result = self.commandList()
			elif self.isCmd(cmd, "RETR"):
				result = self.commandRetr()
			elif self.isCmd(cmd, "CWD"):
				result = self.commandCwd()
			elif self.isCmd(cmd, "DELE"):
				result = self.commandDele()
			elif self.isCmd(cmd, "QUIT"):
				result = self.commandQuit()
		except StateException:
			pass
		
		return result + "\r\n"
	
	def commandUser(self):
		self.assertState(self.S_STATE_CONNECTED)
		self.setState(self.S_STATE_LOGGED)
		return "230 Fake login ok"
	
	def commandPasv(self):
		self.assertState(self.S_STATE_LOGGED)
		self.setState(self.S_STATE_WAITING_DATA_CONNECTION)
		return "227 Entering Fake Passive Mode (5,5,5,5,10,10)"
	
	def commandCwd(self):
		self.assertState(self.S_STATE_LOGGED)
		return "200 Directory changed to whatever"
	
	def commandDele(self):
		self.assertState(self.S_STATE_LOGGED)
		return "200 Whatever file deleted"
	
	def commandQuit(self):
		# valid for any state
		return "200 goodbye"
	
	def greeting(self):
		self.assertState(self.S_STATE_CONNECTED)
		return "220 (fake ftp server)"
	
	def commandList(self):
		if self.state == self.S_STATE_LIST_TRANSFER_DONE:
			self.setState(self.S_STATE_LOGGED)
			self.order = None
			return "250 List sent"
		
		if self.experimentErrorListing:
			# This experiment helped to discover the following bug in client:
			# The connection cleanup was not allowed in state_data_connection_established.
			self.assertState(self.S_STATE_DATA_CONNECTION_ESTABLISHED)
			self.setState(self.S_STATE_LOGGED)
			self.order = None
			return "500 Error listing"
		else:
			self.assertState(self.S_STATE_DATA_CONNECTION_ESTABLISHED)
			self.setState(self.S_STATE_TRANSFERING)
			self.order = self.ORDER_LISTING
			return "150 Here comes the fake directory lising."
	
	def commandRetr(self):
		if self.state == self.S_STATE_FILE_TRANSFER_DONE:
			self.setState(self.S_STATE_LOGGED)
			self.order = None
			return "225 Fake transfer complete"
		
		self.assertState(self.S_STATE_DATA_CONNECTION_ESTABLISHED)
		self.setState(self.S_STATE_TRANSFERING)
		self.order = "xx" # a filename
		return "150 Here comes the fake file."
	
	def setCommand(self, command):
		self.command = command
		
	def getData(self):
		self.assertState(self.S_STATE_TRANSFERING)
		if self.order is None:
			return None # error
		elif self.order == self.ORDER_LISTING:
			return self.getListingData()
		else:
			return self.getFileData()
	
	def closeData(self):
		if self.state == self.S_STATE_FILE_TRANSFER_DONE:
			return True;
		else:
			self.assertState(self.S_STATE_TRANSFERING)
			self.setState(self.S_STATE_FILE_TRANSFER_DONE)
			return True;
		

	def getListingData(self):
		self.assertState(self.S_STATE_TRANSFERING)
		self.setState(self.S_STATE_LIST_TRANSFER_DONE)
		result = (
		  "drwxrwxr-x  283 0        3003        12288 Aug 30 18:45 gnu\r\n"
		+ "-rwxrwxr-x  283 0        3003        12288 Aug 30 18:46 xx\r\n")
		return result

	def getFileData(self):
		self.assertState(self.S_STATE_TRANSFERING)
		self.setState(self.S_STATE_FILE_TRANSFER_DONE)
		result = "THIS IS A FILE\r\nENJOY.";
		return result

		
		
		
		
		
		
		
		
		
		
			
