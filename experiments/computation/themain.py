from sys import argv
from math import pi, sin

from parlib.directive import POSIX
#from parlib.rmath import sin #supported only for C, does not bring a speedup

def computation_poly():
	result = 0.0
	delta = 1e-9
	start = 0.0
	stop = 1.0
	x = start
	while x <= stop:
		y = (x * x + 7.0 * x + 1) / 3.0
		result += delta * y
		x += delta
	
	return result

def computation_sin():
	result = 0.0
	delta = 1e-8
	start = 0.0
	stop = pi/2.0
	x = start
	while x <= stop:
		y = sin(x)
		result += delta * y
		x += delta
	
	return result


def main(argv):				
	try:
		n = int(argv[1])
	except:
		n = 0
	if n == 0:
		x = computation_poly()
	elif n == 1:
		x = computation_sin()
	else:
		x = -1
	print n, " ", x

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
