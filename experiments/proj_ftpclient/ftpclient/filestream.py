from parlib.net.inetworkreader import INetworkReader

class FileStream:
	def __init__(self, reader, machine):
		self.reader = reader
		self.machine = machine
		self.lastPiece = 0

	def read(self):
		self.lastPiece = self.reader.read()

		if self.lastPiece == INetworkReader.CODE_ERR:
			# maintain standard interface
			return INetworkReader.CODE_END

		return self.lastPiece

	def close(self):
		self.reader.close()
		if self.lastPiece == INetworkReader.CODE_END:
			suc = self.machine.transferSuccessfullyDone()
			if not suc:
				#INJECT the same error as in Client.retrieveFile
				# READLINE_LEVEL = 1 is sufficient
				self.machine.dataConnectionClearAfterError()
		elif self.lastPiece == INetworkReader.CODE_ERR:
			self.machine.dataConnectionClearAfterError()
		else:
			# closing in the middle
			# this is assumed as success
			suc = self.machine.transferSuccessfullyDone()
			if not suc:
				self.machine.dataConnectionClearAfterError()
