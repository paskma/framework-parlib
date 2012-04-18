
class FtpFile:
	def __init__(self, name, isdirectory):
		self.name = name
		self.isdirectory = isdirectory
	
	def getName(self):
		return self.name
	
	def isDirectory(self):
		return self.isdirectory
	
	def toString(self):
		result = self.getName()
		if (self.isDirectory()):
			result += " <DIR>"
		
		return result
