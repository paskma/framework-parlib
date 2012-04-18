
class Response:
	def __init__(self, code, lines):
		self.code = code
		self.lines = lines
	
	def toString(self):
		return str(self.code) + "'" + self.lines[0] + "' (and " + str(len(self.lines) - 1) + " more)"
	
	def firstDigit(self):
		return self.code / 100
	
	def isPositivePreliminary(self):
		return self.firstDigit() == 1
	
	def isPositiveCompletion(self):
		return self.firstDigit() == 2

	def isPositiveIntermediate(self):
		return self.firstDigit() == 3

	def isNegativeTransient(self):
		return self.firstDigit() == 4

	def isNegativeCompletion(self):
		return self.firstDigit() == 5
	
	def getDataSocket(self):
		line = self.lines[0]
		data = line[3:]
		
		i = 0;
		while i < len(data):
			if data[i].isdigit():
				break
			i += 1
		
		numbers = []

		current = ""
		while i < len(data):
			c = data[i]
			if c.isdigit():
				current += c
			else:
				if current:
					numbers.append(current)
				current = ""
			i += 1
		
		if current:
			numbers.append(current)
		
		if len(numbers) != 6:
			return None
		
		hostname = "%s.%s.%s.%s" % (numbers[0], numbers[1], numbers[2], numbers[3])
		port = int(numbers[4]) << 8 | int(numbers[5])
		
		return DataSocket(hostname, port)
		
		
	

class DataSocket:
	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port
	
	def toString(self):
		return self.hostname + ":" + str(self.port)
