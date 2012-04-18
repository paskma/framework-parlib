
from parlib.directive import TRANSLATED

from test import test_integration
from ftpclient.statemachine import StateException
from test.server import StateException as ServerStateException

if not TRANSLATED:
	import traceback

class Application:
	"""Do all the offline stuff.
	- transferable to java
	- generated java classes can by wired by pure ftpclient networking
	"""
	def main(self, argv):
		try:
			test_integration.main()
		except StateException, ex:
			print ex.message
			if not TRANSLATED: traceback.print_exc()
		except ServerStateException, ex:
			print ex.message
			if not TRANSLATED: traceback.print_exc()
		
		print "Wiring..."
		print test_integration.wiring()
		print "Integration Done."	
		return 0
