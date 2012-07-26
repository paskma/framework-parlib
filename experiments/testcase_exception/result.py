from parlibutil.locking import Monitor, synchronized


class Result(Monitor):
	def __init__(self):
		Monitor.__init__(self)
		self.value = 0

	@synchronized	
	def put(self, value):
		if value <= self.value:
			raise ValueError
		
		self.value = value
	
	@synchronized
	def get(self):
		return self.value
