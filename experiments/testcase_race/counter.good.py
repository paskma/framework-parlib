from parlibutil.locking import Monitor, synchronized

class Counter(Monitor):
	def __init__(self):
		Monitor.__init__(self)
		self.value = 0
	
	@synchronized
	def inc(self):
		self.value += 1
	
	@synchronized
	def getValue(self):
		return self.value
