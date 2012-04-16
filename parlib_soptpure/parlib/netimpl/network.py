
import socket

from parlib.net.inetwork import INetwork
from parlib.netimpl.networkreader import NetworkReader

class Network(INetwork):
	def __init__(self):
		self.s = None
	
	def connect(self, host, port):
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.connect((host, port))
			return True
		except socket.error:
			self.s.close()
			return False
		
	def sendMessage(self, message):
		try:
			n = self.s.sendall(message)
			#print "sent:", message
			#flush?
			return True
		except socket.error:
			return False
	
	def createNetworkReader(self):
		return NetworkReader(self.s)
	
	def setTimeout(self, timeoutmillis):
		self.s.settimeout(timeoutmillis / 1000.0)
		return True

