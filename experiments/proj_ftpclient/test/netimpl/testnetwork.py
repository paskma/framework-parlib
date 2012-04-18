
from parlib.net.inetwork import INetwork
from test.netimpl.testnetworkreader import TestNetworkReader

class TestNetwork(INetwork):
	def __init__(self, server, data):
		self.server = server
		self.data = data
	
	def connect(self, host, port):
		if self.data:
			self.server.connectToData()
		else:
			self.server.connectToCommand()
		
		return True
		
	def sendMessage(self, message):
		print "sent* ", message
		self.server.setCommand(message)
		return True
	
	def createNetworkReader(self):
		return TestNetworkReader(self.server)
	
	def setTimeout(self, timeoutmillis):
		return True

