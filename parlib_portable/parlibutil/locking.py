from parlib.directive import POSIX
if POSIX:
	from parlib.rthreading import Condition
	from parlib.rthreading import Lock

class Synchronized:
	"""
	For classes that do not require wait/notify.
	"""
	def __init__(self):
		if POSIX: self.lock = Lock();
	def MONITOR_ENTER(self):
		if POSIX: self.lock.MONITOR_ENTER()
	def MONITOR_EXIT(self):
		if POSIX: self.lock.MONITOR_EXIT()

class Monitor:
	def __init__(self):
		if POSIX: self.lock = Condition()
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

def synchronized(meth):
	"""
	Decorator for synchronization.
	Requires either Monitor or Synchronized to be mixed in.
	"""
	def synchronized_meth(self, *args):
		try:
			self.MONITOR_ENTER()
			return meth(self, *args)
		finally:
			self.MONITOR_EXIT()
	return synchronized_meth

def fake_synchronized(meth):
	"""
	Decorator that does nothing. For experimenting.
	"""
	def synchronized_meth(self, *args):
		return meth(self, *args)
	return synchronized_meth
