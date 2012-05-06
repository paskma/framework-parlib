
from parlib.net.inetwork import INetwork
from test.netimpl_random.testnetworkreader import RandTestNetworkReader as TestNetworkReader

from parlib.verify import random
import test.random_config as config

class RandTestNetwork(INetwork):
	def __init__(self, server, data):
		self.server = server
		self.data = data
	
	def connect(self, host, port):
		if config.CONNECT_LEVEL == 1:
			if random(1) == 0:
				return False
		
		if self.data:
			self.server.connectToData()
		else:
			self.server.connectToCommand()
		
		return True
		
	def sendMessage(self, message):
		if config.WRITE_LEVEL == 1:
			if random(1) == 0:
				print "not sent*"
				return False
	
		print "sent* ", message
		self.server.setCommand(message)
		return True
	
	def createNetworkReader(self):
		return TestNetworkReader(self.server)

	def setTimeout(self, timeoutmillis):
		return True
