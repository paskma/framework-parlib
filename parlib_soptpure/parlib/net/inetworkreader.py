
class INetworkReader:
	CODE_END = -1
	CODE_ERR = -2
	# prevent DoS
	# for telnet-like protocol, this is the longest possible valid line
	MAX_LINE_LEN = 128*1024

	def readLine(self):
		buf = ""
		counter = 0
		while True:
			c = self.read()
			if c == self.CODE_END:
				return buf
			if c == self.CODE_ERR:
				return None

			char = chr(c)
			buf += char			
			if char == "\n":
				return buf
			
			counter += 1
			if counter == INetworkReader.MAX_LINE_LEN:
				# It is better to signal error than return incomplete data
				# that appears OK
				return None
	
	def readAll(self):
		return None
	
	def read(self):
		return self.CODE_END
	
	def close(self):
		return False
