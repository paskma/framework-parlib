from parlib.verify import random

from parlib.net.inetworkreader import INetworkReader
import test.random_config as config

def mild_randomization(s):
	r = random(2)
	if r == 0:
		return None
	elif r == 1 and len(s) > 0:
		return s[0]
	else:
		return s

def full_randomization(s):
	l = len(s)
	stop = random(l+1)
	assert stop >= 0 # annotation help
	
	if stop == l+1:
		return None
	else:
		return s[0:stop]

class RandTestNetworkReader(INetworkReader):
	def __init__(self, server):
		self.readPos = 0
		self.readBuffer = None
		self.server = server

	def readLine(self):
		resp = self.server.reply()
		if config.READLINE_LEVEL == 0:
			return resp
		elif config.READLINE_LEVEL == 1:
			return mild_randomization(resp)
		else: # ==2
			return full_randomization(resp)

	def readAll(self):
		data = self.server.getData()
		if config.READALL_LEVEL == 0:
			return data
		elif config.READALL_LEVEL == 1:
			return mild_randomization(data)
		else: # ==2
			return full_randomization(data)

	def read(self):
		if self.readBuffer is None:
			self.readBuffer = self.server.getData()

			if config.READCHAR_LEVEL == 0:
				pass
			elif config.READCHAR_LEVEL == 1:
				self.readBuffer = mild_randomization(self.readBuffer)
			else: # ==2
				self.readBuffer = full_randomization(self.readBuffer)

		if self.readBuffer is None:
			return INetworkReader.CODE_ERR

		if self.readPos == len(self.readBuffer):
			return INetworkReader.CODE_END
			
		result = ord(self.readBuffer[self.readPos])
		self.readPos += 1
		return result

	def close(self):
		return self.server.closeData()
