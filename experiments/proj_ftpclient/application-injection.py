
from parlib.directive import TRANSLATED

from test import test_injection
from ftpclient.statemachine import StateException
from test.server import StateException as ServerStateException

if not TRANSLATED:
	import traceback

class Application:
	"""
	Demo for bug-injection.
	Use  application-integration.py to build osgi jar
	that is also capable of bug-injection.
	"""
	def main(self, argv):
		try:
			test_injection.main()
		except StateException, ex:
			print ex.message
			if not TRANSLATED: traceback.print_exc()
		except ServerStateException, ex:
			print ex.message
			if not TRANSLATED: traceback.print_exc()
		
		print "Injection Done."	
		return 0
