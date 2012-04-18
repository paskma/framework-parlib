from parlib.netimpl.network import Network
from ftpclient.client import Client

def wild_connnection_experiment():
	commandNet = Network()
	dataNet = Network()
	client = Client(commandNet, dataNet)
	client.connect("ftp.gnu.org", 21)
	timeoutset = commandNet.setTimeout(1000)
	if not timeoutset:
		print "Timeout not set"
		return False
	
	connected = client.isConnected()	
	if not connected:
		print "Not connected"
		return False
	
	logged = client.login("anonymous", "osgiftp@kiv.zcu.cz")
	if not logged:
		print "Not logged"
		return False
	
	files = client.listFiles()
	if files is not None:
		for i in files:
			print i.toString()
	else:
		print("No listing obtained.")
		return False
	
	print client.retrieveFile("README")
	
	## Streaming..
	"""
	stream = client.retrieveFileStream("README")
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
	"""
	
	return True
	
