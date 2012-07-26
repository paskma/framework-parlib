from parlibutil.threading import Thread

class Worker(Thread):
	def __init__(self, resource):
		Thread.__init__(self)
		self.resource = resource        

	def run(self, *args):
		self.resource.cascadeLock()
		print "Thread finished without deadlocking."
