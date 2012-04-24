from parlib.rthreading import Thread
from parlib.logging import p
from parlib.rtime import sleep
from parlib.directive import POSIX

class Clock(Thread):
	def __init__(self, summarizer):
		if POSIX: Thread.__init__(self, Clock)
		self.summarizer = summarizer
	
	def tic(self):
		print ">>tic"
		self.summarizer.intervalElapsed()
	
	def RUN(self, *args):
		self.release_bootlock()
		
		limit = 1
		counter = 0
		while True:
			if counter == limit:
				break
			self.tic()
			counter += 1
