

class _Rand(object):
	def __init__(self):
		self.m = 101
		self.a = 31
		self.b = 7
		self.seed = 1
		self.counter = 0
	
	def rand(self):
		self.seed = (self.a * self.seed + self.b) % self.m
		self.counter += 1
		return self.seed

	def random(self):
		#return float(self.rand()) / float(self.m)
		return self.rand() / self.m

_rand = _Rand()

def random():
	#return _rand.random()
	return 0
