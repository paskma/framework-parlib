
from parlib.directive import TRANSLATED

from test import test_integration
from test import test_injection
from test import test_random
from test import test_random_cut
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
			print "=Simple integration"
			test_integration.main()
		except StateException, ex:
			print ex.message
			if not TRANSLATED: traceback.print_exc()
		except ServerStateException, ex:
			print ex.message
			if not TRANSLATED: traceback.print_exc()
		
		print "=Wiring..."
		print test_integration.wiring()
		
		print "=Injected bug..."
		try:
			test_injection.main(True)
		except StateException, ex:
			print "Expected exception, Ok."
		
		try:
			test_injection.main(False) #suppress aggresive optimization
		except StateException, ex:
			print "Expected exception, Ok."
		
		print "=Random part..."
		try:
			test_random.main()
		except StateException, ex:
			print "Exception is randomly possible"
			
		
		print "=Random part (cut)..."
		try:
			test_random_cut.main()
		except StateException, ex:
			print "Exception is randomly possible"
		
		
		print "=Integration Done."
		return 0
