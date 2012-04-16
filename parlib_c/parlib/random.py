from time import time
from math import floor

class _Rand(object):
	def __init__(self):
		self.m = 101
		self.a = 31
		self.b = 7
		self.seed = 1
		self.clock_seed = False
	
	def oneshotClockSeed(self):
		if not self.clock_seed:
			t = time()
			self.seed = int((t - floor(t))*100.0)
			self.clock_seed = True
	
	
	def rand(self):
		self.seed = (self.a * self.seed + self.b) % self.m
		return self.seed

	def random(self):
		#return float(self.rand()) / float(self.m)
		return self.rand() / self.m

_rand = _Rand()

def random():
	_rand.oneshotClockSeed()
	return _rand.rand()
