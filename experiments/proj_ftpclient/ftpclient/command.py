
class Command:
	def __init__(self, command, argument):
		self.command = command
		self.argument = argument
	
	def toString(self):
		if self.argument is None:
			return "%s\r\n" % self.command
		else:
			return "%s %s\r\n" % (self.command, self.argument)
	

def USER(username):
	return Command("USER", username)

def PASS(password):
	return Command("PASS", password)

def PASV():
	return Command("PASV", None)

def LIST():
	return Command("LIST", None)

def CWD(dirname):
	return Command("CWD", dirname)

def RETR(filename):
	return Command("RETR", filename)

def DELE(filename):
	return Command("DELE", filename)

def QUIT():
	return Command("QUIT", None)
