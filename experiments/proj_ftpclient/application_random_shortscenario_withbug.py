from test import test_random_shortscenario
from ftpclient.statemachine import StateException
from test.server import StateException as ServerStateException
#import traceback

class Application:
	"""
	Experiment with Verify.random*
	For counting of states of JPF and comparison with simulation
	"""
	def main(self, argv):
		try:
			test_random_shortscenario.main(True)
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
