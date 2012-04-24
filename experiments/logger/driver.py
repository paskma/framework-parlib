from parlib.rthreading import Thread
from parlib.directive import POSIX

from event import Event

class Driver(Thread):
	def __init__(self, device, summarizer):
		if POSIX: Thread.__init__(self, Driver)
		self.summarizer = summarizer
		self.device = device
	
	def RUN(self, *arg):
		self.release_bootlock()
		
		limit = 1
		counter = 0
		while True:
			if counter == limit:
				break
			self.eventOccured()
			self.alarmOccurred()
			counter += 1
	
	def alarmOccurred(self):
		self.summarizer.handleAlarm()
	
	def eventOccured(self):
		print ">>occured"
		event = Event(self.device, 0, 1)
		self.summarizer.handleEvent(event)
