from test.server import Server
from test.netimpl.testnetwork import TestNetwork
from parlib.net.inetwork import INetwork
from ftpclient.client import Client

def main():
	server = Server()
	commandNet = TestNetwork(server, False)
	dataNet = TestNetwork(server, True)
	host = "foo"
	client = Client(commandNet, dataNet)
	suc = client.connect(host, 21)
	print "C:Test connected:", suc
	client.login("anonymous", "osgiftp@kiv.zcu.cz")
	files = client.listFiles()
	if files is not None:
		for i in files:
			print i.toString()
	else:
		print("C:No listing obtained.")
	
	f = client.retrieveFile("xx")
	if f is not None:
		print "C:File is:\r\n", f
	else:
		print "C:File transfer failed."

	print "C:Testing stream api..."
	stream = client.retrieveFileStream("xx")
	buf = ""
	print "C:reading from stream byte by byte"
	c = stream.read()
	while c != -1:
		buf += chr(c);
		c = stream.read()
	
	print "C:closing stream"	
	stream.close();
	print "C:File from stream:"
	print buf
	

	print "C: ask and close"
	stream = client.retrieveFileStream("xx2")
	stream.close();
	
	
	print "C:Healthy?"
	f = client.retrieveFile("xx2") # suppress aggresive optimization
	print "C:", (file is not None)
	
	client.changeWorkingDirectory("a_dir")
	client.changeWorkingDirectory("b_dir") # suppress aggresive optimization
	
	client.deleteFile("a_file")
	client.deleteFile("b_file") #suppress aggresive optimization
	
	client.logout()
	
	print "C:TestDone."

def wiring():
	commandNet = INetwork()
	dataNet = INetwork()
	client = Client(commandNet, dataNet)
	client.connect("bar", 122)
	return (client.isConnected(), client.isLogged())
	
