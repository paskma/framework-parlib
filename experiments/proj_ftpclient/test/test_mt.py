from parlibutil.threading import Thread

from test.server import Server
from test.netimpl.testnetwork import TestNetwork
from ftpclient.client import Client
from ftpclient.statemachine import StateException


class Worker(Thread):

	def __init__(self, stream):
		Thread.__init__(self)
		self.stream = stream

	def run(self, *args):
		buf = ""
		print "CT:reading from stream byte by byte "
		c = self.stream.read()
		while c != -1:
			buf += chr(c);
			c = self.stream.read()
	
		print "CT:closing stream"	
		self.stream.close(); ## INJECTION: comment this line for bug injection
		print "CT:File from stream:"
		print buf
		print "CT:thread finished"
		


def main():
	""" This test demostrates that
		- the tracker is properly synchronized (chec_race)
		- StateException is raised until stream is not closed
	"""
	server = Server()
	#server.setExperimentErrorListing(true);
	commandNet = TestNetwork(server, False)
	dataNet = TestNetwork(server, True)
	host = "foo"
	client = Client(commandNet, dataNet)
	suc = client.connect(host, 21)
	print "C:Test connected:", suc
	client.login("anonymous", "osgiftp@kiv.zcu.cz")

	print "C:Testing stream api (MT)..."
	stream = client.retrieveFileStream("xx")

	worker = Worker(stream)
	worker.start()
	
	f = None	
	try:
		# we either succeed fully or raise StateException
		f = client.retrieveFile("xx2")
		assert (f is not None)
	except StateException:
		# this operation may fail if the thread is not finished
		# raising an exception is correct behavior
		pass

	print "C:", (file is not None)

	print "C:joining thread"	
	worker.join() ## INJECTION: comment this line to inject a bug
	
	# these operation never fail
	# because we have joined the thread
	suc = client.changeWorkingDirectory("a_dir")
	assert (suc == True)
	suc = client.changeWorkingDirectory("b_dir")
	assert (suc == True)

	print "C:TestDone."
