#
from pypy.module.thread.ll_thread import start_new_thread, allocate_lock
#from ll_pasys import ll_thread_start, ll_allocate_lock, ll_acquire_lock, ll_release_lock, ll_dump


def ll_dump(x):
	print x

class Lock(object):
	def __init__(self):
		self.lock = allocate_lock()
	def acquire(self, flag=True):
		self.lock.acquire(flag)
	def release(self):
		self.lock.release()

class Condition(object):
	def __init__(self):
		print "Condition::init"
		self.lock = Lock()
		self.acquire = self.lock.acquire
		self.release = self.lock.release
		self.waiters = []
	
	def wait(self):
		print "Condition::wait"
		waiter = Lock()
		waiter.acquire()
		self.waiters.append(waiter)
		self.lock.release()
		waiter.acquire()
	
	def notify(self):
		print "Condition::notify"
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
		ll_dump("BOOTSTRAP")
		boot.proc(boot.body)
	
	bootstrap = staticmethod(bootstrap)

boot = _Bootstrapper()

def init_threads():
	boot.lock = Lock()
	print "Lock inited", boot.lock

def release_bootlock():
	boot.lock.release()

class Thread:
	def __init__(self, subclass):
		self.subclass = subclass
	
	def start(self):
		#ll_acquire_lock(boot.lock)
		boot.lock.acquire()
		boot.body = self
		boot.proc = self.subclass.run
		#boot.bootstrap()
		start_new_thread(boot.bootstrap, ())
		#ll_thread_start(boot.bootstrap)
		#ll_release_lock(boot.lock)
		#from rtime import sleep
		#sleep(1)
		#boot.lock.release()
	
	def release_bootlock(self):
		release_bootlock()
		
	def run(self, *args):
		print "DUMMY RUN"
	
	def setDaemon(self, isDaemon):
		pass

class SubclassThread(Thread):
	def __init__(self):
		Thread.__init__(self, SubclassThread)
		
	def run(*args):
		print "CLEVER RUN"

#def _shutdown():
#	print "SHUTDOWN"
if __name__ == "__main__":
	t = SubclassThread()
	t.start()
	print "Done"
