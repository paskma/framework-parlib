from test import Test

class FirstTest(Test):
	def firstTest(self):
		self.assertEqualsInt(4, 2+2)
		self.assertEqualsInt(4, 1+1)
		self.assertEqualsStr("ab", "a" + "b")
		self.assertEqualsStr("ab", "a" + "x")
		self.assertEqualsBool(True, False or True)
	
	def run(self):
		self.firstTest()
		

