
from rthreading import boot
from foo import dumpln

LOG_AVAIL = ["all", "blekota"]

def p(s, klass="all"):
	pass
	#if klass in LOG_AVAIL:
		#boot.lock.acquire()
		#dumpln(s)
		#pass
		#boot.lock.release()
	#pass

def test():
	p("single")
	p("p" + " test")
	p("not avail!!", "mekota")
	p("next line" + " 2", "blekota")

if __name__ == "__main__":
	test()
	
def entry_point(argv):
	test()
	return 0

def target(*args):
	return entry_point, None
