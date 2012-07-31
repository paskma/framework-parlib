from test import Test

class ReturnFinallyTest(Test):
	
	def foo(self, n):
		try:
			return n - 1
		finally:
			if n == 55:
				return -555
	

	def returnFinallyTest(self):
		self.message("-returnFinallyTest")
		self.assertEqualsInt(self.foo(1), 0)
		self.assertEqualsInt(self.foo(2), 1)
		self.assertEqualsInt(self.foo(3), 2)
		self.assertEqualsInt(self.foo(55), -555)
	
	def run(self):
		self.returnFinallyTest()
		

