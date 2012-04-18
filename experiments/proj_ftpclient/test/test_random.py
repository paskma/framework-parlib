from test.server_random import Server
from test.netimpl_random.testnetwork import TestNetwork
from ftpclient.client import Client
from ftpclient.statemachine import StateException


def main():
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
	
	f = client.retrieveFile("xx")
	if f is None:
		pass
	else:
		print f
		
	f = client.retrieveFile("xx2")
	if f is None:
		pass
	else:
		print f
	
	
	stream = client.retrieveFileStream("xx")
	buf = ""
	if stream is not None:
		c = stream.read()
		while c != -1:
			buf += chr(c);
			c = stream.read()
	
		stream.close();
		print buf
		
	suc = client.changeWorkingDirectory("b_dir")
	if not suc:
		pass
	
	suc = client.deleteFile("a_file")
	if not suc:
		pass
	
	suc = client.logout()
	if not suc:
		pass

	print "C:TestDone."
