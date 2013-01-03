from test.server import Server
from test.netimpl.testnetwork import TestNetwork
from parlib.net.inetwork import INetwork
from ftpclient.client import Client

def main(clientBug):
	server = Server()
	server.setExperimentErrorDataTransferConfirmation(True)
	commandNet = TestNetwork(server, False)
	dataNet = TestNetwork(server, True)
	host = "foo"
	client = Client(commandNet, dataNet)
	client.setDataTransferConfirmationBug(clientBug)
	client.setPasvResponseReadingBug(clientBug)
	suc = client.connect(host, 21)
	print "C:Test connected:", suc
	client.login("anonymous", "osgiftp@kiv.zcu.cz")
	
	f = client.retrieveFile("xx")
	if f is not None:
		print "C:File is:\r\n", f
	else:
		print "C:File transfer failed."

	print "C:##Second shot..."
	
	f = client.retrieveFile("xx")
	if f is not None:
		print "C:File is(2):\r\n", f
	else:
		print "C:File transfer failed.(2)"
	
	print "C:##Third shot..."
	
	f = client.retrieveFile("xx")
	if f is not None:
		print "C:File is(3):\r\n", f
	else:
		print "C:File transfer failed.(3)"
	
	print "C:##Stream shot..."	
	
	stream = client.retrieveFileStream("xx")
	counter = 0
	while True:
		c = stream.read()
		if c == -1:
			stream.close()
			break
		else:
			counter += 1

	print "Stream contained %d bytes" % counter
	
	client.logout()
	
	print "C:TestDone."
