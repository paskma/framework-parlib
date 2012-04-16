
class Loop:
	def ALLWAYS_FALSE(self, a, b):
		self.ALLWAYS_FALSE_IMPL(a, b)
		return a==b

	def FAKE_INC(self, a):
		self.FAKE_INC_IMPL(a)
		return a+1
	
	def ALLWAYS_FALSE_IMPL(self, a, b):
		return False
	
	def FAKE_INC_IMPL(self, a):
		return a
