
from parlib.net.inetwork import INetwork
from test.netimpl_random.testnetworkreader import RandTestNetworkReader as TestNetworkReader
from test.server_random import RandServerConfig

from parlib.verify import random

class RandTestNetwork(INetwork):
	def __init__(self, server, data, randServerConfig=None):
		self.server = server
		self.data = data
		if randServerConfig is None:
			self.config = RandServerConfig()
		else:
			self.config = randServerConfig
	
	def connect(self, host, port):
		if self.config.CONNECT_LEVEL == 1:
			if random(1) == 0:
				return False
		
		if self.data:
			self.server.connectToData()
		else:
			self.server.connectToCommand()
		
		return True
		
	def sendMessage(self, message):
		if self.config.WRITE_LEVEL == 1:
			if random(1) == 0:
				print "not sent*"
				return False
	
		print "sent* ", message
		self.server.setCommand(message)
		return True
	
	def createNetworkReader(self):
		return TestNetworkReader(self.server, self.config)

	def setTimeout(self, timeoutmillis):
		return True
