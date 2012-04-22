from parlib.rtime import sleep
from parlib.directive import POSIX

from creator import Creator

def main(argv):
	n = 100000
	loops = 1000
	threads = 0
	if len(argv) >= 4:
		n = int(argv[1])
		loops = int(argv[2])
		threads = int(argv[3])
		
	c = Creator(n, loops)
	if threads == 1:
		c.start()
		sleep(1000.0)
	else:
		c.body()

if __name__ == "__main__":
	from sys import argv
	main(argv)

def entry_point(argv):
	if POSIX:
		from parlib.rthreading import init_threads
		init_threads()
	main(argv)
	return 0

def target(*argv):
	return entry_point, None
