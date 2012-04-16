from parlib.net.inetworkreader import INetworkReader
import foo

class NetworkReader(INetworkReader):
	def __init__(self, slot):
		self.slot = slot
		
	def readAll(self):
		buf = ""
		while True:
			c = self.read()
			if c == self.CODE_END:
				return buf
			if c == self.CODE_ERR:
				return None

			char = chr(c)
			buf += char
	
	def read(self):
		c = foo.simplenet_read(self.slot)
		if c == -1:
			return self.CODE_END
		if c == -2:
			return self.CODE_ERR
		
		return c
		
	def close(self):
		suc = foo.simplenet_close(self.slot)
		return suc >= 0
