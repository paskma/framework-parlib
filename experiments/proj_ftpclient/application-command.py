
from command_client import CommandClient

class Application:
	def main(self, argv):
		commandClient = CommandClient()
		commandClient.run()
		print "Command client done."	
		return 0
