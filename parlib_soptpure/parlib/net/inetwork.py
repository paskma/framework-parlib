from parlib.net.inetworkreader import INetworkReader

class INetwork:
	def connect(self, host, port):
		return False
	
	def sendMessage(self, message):
		return False
	
	def createNetworkReader(self):
		return INetworkReader();
	
	def setTimeout(self, timeoutmillis):
		return False

