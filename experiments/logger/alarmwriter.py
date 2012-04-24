from parlib.rthreading import Thread
from parlib.logging import p
from parlib.rtime import sleep
from parlib.directive import POSIX

class AlarmWriter(Thread):
	def __init__(self, summarizer):
		if POSIX: Thread.__init__(self, AlarmWriter)
		self.summarizer = summarizer
	
	def RUN(self, *args):
		self.release_bootlock()
		
		limit = 1
		counter = 0
		while True:
			if counter == limit:
				break
			self.summarizer.waitAndWriteAlarm()
			counter += 1
