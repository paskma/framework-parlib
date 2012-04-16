
from parlib import rsimplenet

from parlib.net.inetwork import INetwork
from parlib.netimpl.networkreader import NetworkReader

class Network(INetwork):
	def __init__(self):
		self.slot = -1
	
	def connect(self, host, port):
		self.slot = rsimplenet.ll_simplenet_connect(host, port)
		return self.slot >= 0
		
	def sendMessage(self, message):
		suc = rsimplenet.ll_simplenet_write_buf(self.slot, message, len(message))
		return suc == len(message)
	
	def createNetworkReader(self):
		return NetworkReader(self.slot)

	def setTimeout(self, timeoutmillis):
		suc = rsimplenet.ll_simplenet_set_timeout(self.slot, timeoutmillis)
		return suc >= 0
