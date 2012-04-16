from parlib import rthreading
from parlib.directive import POSIX

class Thread(rthreading.Thread):
	"""
		This class is abstract. Overload the run method.
		
		This stays on top or rthreading.Thread. Deals with some
		implementation details (releasing bootlock).
		
		Supports joining.
	"""
	
	def __init__(self):
		if POSIX:
			rthreading.Thread.__init__(self, Thread)
			self.lock = rthreading.Condition();
		self.barrier = False
	
	# TODO: this should be mix-in
	def MONITOR_ENTER(self):
		if POSIX: self.lock.MONITOR_ENTER()
	def MONITOR_EXIT(self):
		if POSIX: self.lock.MONITOR_EXIT()
	def WAIT(self):
		if POSIX: self.lock.WAIT()
	def NOTIFY(self):
		if POSIX: self.lock.NOTIFY()
	def NOTIFYALL(self):
		if POSIX: self.lock.NOTIFYALL()
	
	def run(self, *args):
		print "Should not be here (run)"
		pass
	
	def start(self):
		self.THREAD_STARTED()
		rthreading.Thread.start(self)
	
	def THREAD_STARTED(self):
		self.MONITOR_ENTER()
		self.barrier = True
		self.MONITOR_EXIT()
	
	def THREAD_FINISHED(self):
		self.MONITOR_ENTER()
		self.barrier = False
		self.NOTIFYALL()
		self.MONITOR_EXIT()
	
	def RUN(self, *args):
		self.release_bootlock()
		try:
			self.run(*args)
		finally:
			self.THREAD_FINISHED()
	
	def join(self):
		self.MONITOR_ENTER()
		while (self.barrier):
			self.WAIT()
		self.MONITOR_EXIT()
