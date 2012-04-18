from parlib.console import Console
from ftpclient.client import Client
from ftpclient.statemachine import StateException

from parlib.netimpl.network import Network
#from test.netimpl.testnetwork import TestNetwork as Network
#from test.server import Server

class CommandClient:
	def __init__(self):
		#server = Server()
		#self.commandNet = Network(server, False)
		#self.dataNet = Network(server, True)
		self.commandNet = Network()
		self.dataNet = Network()
		self.client = Client(self.commandNet, self.dataNet)


	def run(self):
		console = Console()
		while True:
			print "@Enter command:"
			command = console.readLine()
			print "@Command was: '%s'" % command
			
			quit = False
			try:
				quit = self.dispatchCommand(command)
			except StateException, ex:
				print "@State exception: %s" % ex.toString()
			except Exception, ex:
				print "@General exception.", ex
			
			if quit:
				break
	
	def dispatchCommand(self, command):
		if command == "quit":
			return True
			
		if command.startswith("open"):
			self.commandOpen(command[len("open")+1:])
		elif command.startswith("login"):
			self.commandLogin()
		elif command.startswith("ls"):
			self.commandLs()
		elif command.startswith("cd"):
			self.commandCd(command[len("cd")+1:])
		elif command.startswith("cat"):
			self.commandCat(command[len("cat")+1:])
		elif command.startswith("scat"): # stream cat
			self.commandScat(command[len("scat")+1:])
		elif command.startswith("rm"):
			self.commandRm(command[len("rm")+1:])
		elif command.startswith("bye"):
			self.commandBye()
		elif command.startswith("help"):
			print "Commands: open, login, ls, cd, cat, scat, rm, bye, quit."
		else:
			print "Command not understood."
			
		return False

	def commandCd(self, directory):
		print "@Changing to dir '%s'" % directory
		suc = self.client.changeWorkingDirectory(directory)
		if suc:
			print "@Directory changed."
		else:
			print "@Error changing directory."
	
	def commandBye(self):
		print "@Requesting quit."
		suc = self.client.logout()
		if suc:
			print "@Quit done."
		else:
			print "@Error quitting."

	def commandCat(self, filename):
		print "@retrieving file '%s'" % filename
		f = self.client.retrieveFile(filename)
		if f is None:
			print "@Error getting file."
		else:
			print "@File content:"
			print f
			print "@End file content."
	
	def commandScat(self, filename):
		""" stream cat """
		
		print "@retrieving file (stream) '%s'" % filename
		stream = self.client.retrieveFileStream(filename)
		if stream is None:
			print "@Error getting file."
		else:
			print "@File content:"
			c = stream.read()
			while c != -1:
				print chr(c)
				c = stream.read()
			stream.close()
			print "@End file content."

	def commandOpen(self, hostname):
		print "@Connecting to hostname '%s'" % hostname
		suc = self.client.connect(hostname, 21)
		self.commandNet.setTimeout(3000)
		if suc:
			print "@Connected."
		else:
			print "@Error connecting."
	
	def commandLogin(self):
		print "@Logging in as anonymous/paskma@gmail.com"
		suc = self.client.login("anonymous", "paskma@gmail.com")
		if suc:
			print "@Logged in."
		else:
			print "@Error log in."

		
	def commandLs(self):
		print "@Listing current directory"
		files = self.client.listFiles()
		if files is not None:
			for i in files:
				print i.toString()
		else:
			print("@No listing obtained.")
	
	def commandRm(self, filename):
		print "@Deleting file '%s'" % filename
		suc = self.client.deleteFile(filename)
		if suc:
			print "@Deleted."
		else:
			print "@Error deleting."
