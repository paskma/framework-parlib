from parlibutil.locking import Monitor, synchronized
from parlib.rtime import sleep

class Resource(Monitor):
	def __init__(self):
		Monitor.__init__(self)
		self.secondLevel = None
	
	def setSecondLevel(self, secondLevel):
		self.secondLevel = secondLevel
	
	@synchronized
	def cascadeLock(self):
		print "First level locked"
		sleep(1.0)
		self.secondLevel.lockSecondLevel()
	
	@synchronized
	def lockSecondLevel(self):
		print "Second level locked"
