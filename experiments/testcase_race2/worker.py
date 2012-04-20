from parlibutil.threading import Thread

class Worker(Thread):

	def __init__(self, counter, n):
		Thread.__init__(self)
		self.counter = counter
		self.n = n

	def run(self, *args):
		#print "incrementing"
		for i in range(self.n):
			self.counter.inc()
