
from thread import start_new_thread
from threading import RLock, Lock
from sys import exc_info

class MonitorLock(object):
	def __init__(self):
		self.lock = RLock()
	def acquire(self, flag=True):
		self.lock.acquire()
	def release(self):
		self.lock.release()
	def MONITOR_ENTER(self):
		self.acquire()
	def MONITOR_EXIT(self):
		self.release()

class Condition(object):
	def __init__(self):
		print "Condition::init"
		self.lock = MonitorLock()
		self.MONITOR_ENTER = self.lock.MONITOR_ENTER
		self.MONITOR_EXIT = self.lock.MONITOR_EXIT
		self.waiters = []
	
	def WAIT(self):
		print "Condition::wait"
		waiter = Lock()
		waiter.acquire()
		self.waiters.append(waiter)
		self.lock.MONITOR_EXIT()
		waiter.acquire()    # wait on the second acquisition
		self.lock.MONITOR_ENTER() # reacquire
	
	def NOTIFY(self):
		print "Condition::notify"
		if self.waiters:
			w = self.waiters.pop(0)
			w.release()
	
	def NOTIFYALL(self):
		for i in xrange(len(self.waiters)):
			self.NOTIFY()


def release_boot_lock():
	pass

class Thread:
	def __init__(self, subclass):
		pass
	
	def start(self):
		start_new_thread(self._run, ())
	
	def _run(self):
		try:
			self.RUN()
		except Exception, ex:
			print "Exception in thread:"
			exc_type, exc_value, exc_tb = exc_info()
			while exc_tb:
				print (
					'  File "%s", \n    line %s, in %s' %
					(exc_tb.tb_frame.f_code.co_filename,
					exc_tb.tb_lineno,
					exc_tb.tb_frame.f_code.co_name))
				exc_tb = exc_tb.tb_next
			print ("Type and value: '%s':'%s'" % (exc_type, exc_value))
		
	def RUN(self):
		pass
	
	def release_bootlock(self):
		release_boot_lock()
