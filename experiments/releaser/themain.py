from parlib.directive import POSIX

import body

def main(argv):
	body.main(argv)	

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
