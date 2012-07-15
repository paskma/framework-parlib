from parlib.directive import POSIX
from application import Application

# You do not need to change this file.


def main(argv):
	app = Application()
	return app.main(argv)

if __name__ == "__main__":
	from sys import argv
	main(argv)

def entry_point(argv):
	if POSIX:
		from parlib.rthreading import init_threads
		init_threads()
	return main(argv)

def target(*argv):
	return entry_point, None
