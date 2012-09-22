from test import test_mt
from ftpclient.statemachine import StateException
from test.server import StateException as ServerStateException
#import traceback

class Application:
	"""
	MT experiment
	"""
	def main(self, argv):
		try:
			test_mt.main()
		except StateException, ex:
			print ex.message
			raise
			#traceback.print_exc()
		except ServerStateException, ex:
			print ex.message
			raise
			#traceback.print_exc()
		
		print "MT Done."	
		return 0
