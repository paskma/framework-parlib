from parlib.directive import POSIX
if POSIX:
	from parlib.rthreading import Condition

class Summarizer:
	def MONITOR_ENTER(self):
		if POSIX: self.lock.MONITOR_ENTER()
	def MONITOR_EXIT(self):
		if POSIX: self.lock.MONITOR_EXIT()
	def WAIT(self):
		if POSIX: self.lock.WAIT()
	def NOTIFY(self):
		if POSIX: self.lock.NOTIFY()
		
	def __init__(self, database, alarmLog):
		self.filled = 0
		self.alarm = 0
		self.database = database
		self.alarmLog = alarmLog
		if POSIX:
			self.lock = Condition()
	
	def handleEvent(self, event):
		self.MONITOR_ENTER()
		self.filled = 1
		handleProbe = self.filled
		self.MONITOR_EXIT()
	
	def handleAlarm(self):
		self.MONITOR_ENTER()
		self.alarm += 1
		self.NOTIFY()
		self.MONITOR_EXIT()
	
	def _nothing(self):
		pass
	
	def _clearInterval(self):
		pass
	
	def _pushInterval(self):
		self.database.writeInterval(0, 0, 0)
		self._clearInterval()
		
	
	def intervalElapsed(self):
		self.MONITOR_ENTER()
		flushProbe = self.filled
		
		if (self.filled == 1):
			self._pushInterval()
		else:
			self._nothing()
		self.MONITOR_EXIT()
	
	def waitAndWriteAlarm(self):
		self.MONITOR_ENTER()
		while self.alarm == 0:
			self.WAIT()
		
		self.alarmLog.writeAlarm()
		self.alarm -= 1
		self.MONITOR_EXIT()
		
		
		
		
		
