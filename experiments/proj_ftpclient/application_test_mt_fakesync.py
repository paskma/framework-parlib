
import ftpclient.statemachine_synchronization_config as config

config.USE_FAKE_SYNCHRONIZATION = True

from application_test_mt import Application as OriginalApp

class Application:
	def main(self, argv):
		return OriginalApp().main(argv)
