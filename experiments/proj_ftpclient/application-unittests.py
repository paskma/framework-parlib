from test.unittest import test_command
from test.unittest import test_response
from test.unittest import test_directory_parser

class Application:
	def main(self, argv):
		test_command.main()
		test_response.main()
		test_directory_parser.main()
		print "Unittests Done."	
		return 0
