from parlib.verify import random

from test.server_random import RandServer as Server
from test.netimpl_random.testnetwork import RandTestNetwork as TestNetwork
from ftpclient.client import Client
from ftpclient.statemachine import StateException


def main():
	"""
		Tests various sequences of commands.
	"""
	server = Server()

	commandNet = TestNetwork(server, False)
	dataNet = TestNetwork(server, True)
	host = "foo"
	client = Client(commandNet, dataNet)
	suc = client.connect(host, 21)
	print "C:Test connected:", suc
	if not suc:
		return
	
	suc = client.login("anonymous", "osgiftp@kiv.zcu.cz")
	if not suc:
		return
	
	for i in range(3):
		cmd = random(3)
		if cmd == 0:
			f = client.retrieveFile("xx")
			if f is None:
				pass
			else:
				print f
		elif cmd == 1:
			stream = client.retrieveFileStream("xx")
			buf = ""
			if stream is not None:
				c = stream.read()
				while c != -1:
					buf += chr(c);
					c = stream.read()
	
				stream.close();
				print buf
		elif cmd == 2:
			suc = client.changeWorkingDirectory("b_dir")
			if not suc:
				pass
		elif cmd == 3:
			files = client.listFiles()
			if files is None:
				pass
			
	
	suc = client.logout()
	if not suc:
		pass

	print "C:TestDone (random 2)."
