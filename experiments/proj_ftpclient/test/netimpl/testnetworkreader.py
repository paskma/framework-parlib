from parlib.net.inetworkreader import INetworkReader

class TestNetworkReader(INetworkReader):
	def __init__(self, server):
		self.readPos = 0
		self.readBuffer = None
		self.server = server

	def readLine(self):
		return self.server.reply()

	def readAll(self):
		return self.server.getData()

	def read(self):
		if self.readBuffer is None:
			self.readBuffer = self.server.getData()

		if self.readPos == len(self.readBuffer):
			return INetworkReader.CODE_END;
			
		result = ord(self.readBuffer[self.readPos])
		self.readPos += 1
		return result

	def close(self):
		return self.server.closeData()
