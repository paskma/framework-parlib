from files import File

class Application:
	def main(self, argv):
		f = File()
		f.open()
		f.write()
		# missing f.close()
		#print "Done."
