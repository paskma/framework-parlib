from test import test_random2
from ftpclient.statemachine import StateException
from test.server import StateException as ServerStateException
#import traceback

class Application:
	"""
	Experiment with Verify.random*
	Command sequence variant.
	"""
	def main(self, argv):
		try:
			test_random2.main()
		except StateException, ex:
			#print ex.message
			raise
			#traceback.print_exc()
		except ServerStateException, ex:
			#print ex.message
			raise
			#traceback.print_exc()
		
		print "Random Done."	
		return 0
