
import foo

from parlib.net.inetwork import INetwork
from parlib.netimpl.networkreader import NetworkReader

class Network(INetwork):
	def __init__(self):
		self.slot = -1
	
	def connect(self, host, port):
		self.slot = foo.simplenet_connect(host, port)
		return self.slot >= 0
		
	def sendMessage(self, message):
		suc = foo.simplenet_write_buf(self.slot, message)
		return suc == len(message)
	
	def createNetworkReader(self):
		return NetworkReader(self.slot)

	def setTimeout(self, timeoutmillis):
		suc = foo.simplenet_set_timeout(self.slot, timeoutmillis)
		return suc >= 0
