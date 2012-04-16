import foo

class Console:
	def readLine(self):
		buf = ""
		while True:
			c = self._read()
			if c == -1:
				return buf
			if c == -2:
				return None

			char = chr(c)
			buf += char			
			if char == "\n":
				return buf
	
	def _read(self):
		c = foo.simplecon_get_char()
		return c

