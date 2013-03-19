from test.server_random import RandServer, RandServerConfig
from test.netimpl_random.testnetwork import RandTestNetwork as TestNetwork
from ftpclient.client import Client
from ftpclient.statemachine import StateException


def main(dataTransferConfirmationBug, pasvResponseReadingBug, cuttingServer):
	""" 
		Mainly for counting states of JPF and for comparison with simulation 
	"""
	assert not (dataTransferConfirmationBug and pasvResponseReadingBug)
	
	config = None
	if cuttingServer:
		config = RandServerConfig()
		config.setSERVER_LEVEL(0)
		config.setREADLINE_LEVEL(2)
		
	server = RandServer(config)

	commandNet = TestNetwork(server, False, config)
	dataNet = TestNetwork(server, True)
	host = "foo"
	client = Client(commandNet, dataNet)
	# This sets the artificial clien bug:
	client.setDataTransferConfirmationBug(dataTransferConfirmationBug)
	client.setPasvResponseReadingBug(pasvResponseReadingBug)
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
	
	suc = client.logout()
	if not suc:
		pass

	print "C:TestDone."
