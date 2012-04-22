from files import File

class Application:
	def main(self, argv):
		f = File()
		f2 = File()
		f2.open()
		f.open()
		f.write()
		f2.close()
		# missing f.close()
		#print "Done."
