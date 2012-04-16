
from foo import start_new_thread, allocate_lock, acquire_lock, release_lock

def dump(x):
	pass

class Lock(object):
	def __init__(self):
		self.lock = allocate_lock()
	def acquire(self, flag=True):
		acquire_lock(self.lock)
	def release(self):
		release_lock(self.lock)
	def MONITOR_ENTER(self):
		pass
	def MONITOR_EXIT(self):
		pass

class Condition(object):
	def __init__(self):
		dump("Condition::init")
		self.lock = Lock()
		self.acquire = self.lock.acquire
		self.release = self.lock.release
		self.waiters = []
	
	def wait(self):
		dump("Condition::wait")
		waiter = Lock()
		waiter.acquire()
		self.waiters.append(waiter)
		self.lock.release()
		waiter.acquire()
	
	def notify(self):
		dump("Condition::notify")
		if self.waiters:
			w = self.waiters.pop(0)
			w.release()
	
	def notifyAll(self):
		for i in xrange(len(self.waiters)):
			self.notify()
	
class _Bootstrapper:
	def __init__(self):
		self.body = None
		self.proc = None
	
	def bootstrap():
		dump("BOOTSTRAP")
		#boot.proc(boot.body)
		#boot.body.proc()
		boot.body.run()
	
	bootstrap = staticmethod(bootstrap)

boot = _Bootstrapper()

def init_threads():
	#boot.lock = ll_allocate_lock()
	boot.lock = Lock()
	#print "Lock inited", boot.lock

def release_bootlock():
	boot.lock.release()

def acquire_bootlock():
	boot.lock.acquire()

class Thread:
	def __init__(self, subclass):
		self.subclass = subclass
	
	def start(self):
		boot.lock.acquire()
		boot.body = self
		boot.proc = self.subclass.run
		alwaysTrue = boot.body == self
		#assert alwaysTrue --commented because it gives a hint to translator!
		if not alwaysTrue:
			#dump("NEVER HERE!")
			boot.bootstrap()
			raise AssertionError
		#dump("calling foo.start_new_thread")
		start_new_thread()
		#boot.bootstrap()
		#dump("...start done")
		
	def run(self):
		dump("DUMMY RUN")
	
	def setDaemon(self, isDaemon):
		pass
	
	def release_bootlock(self):
		release_bootlock()
