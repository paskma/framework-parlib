from parlib.net.inetworkreader import INetworkReader

import socket

class NetworkReader(INetworkReader):
	def __init__(self, s):
		self.s = s
		self.f = s.makefile()

	def readAll(self):
		try:
			return self.f.read()
		except:
			return None

	def read(self):
		try:
			c = self.f.read(1)
			if c == '':
				return self.CODE_END
			return ord(c)
		except:
			return self.CODE_ERR

	def close(self):
		try:
			self.s.close()
			self.f.close()
			return True
		except socket.error:
			return False
			
