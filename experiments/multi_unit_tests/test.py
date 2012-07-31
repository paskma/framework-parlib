from parlibutil.reflect import clone_function

class Test:
	def __init__(self):
		self.testCounter = 0;

	def _assertEquals(self, expected, actual):
		self.testCounter += 1
		
		if expected == actual:
			self.report_success()
		else:
			self.report_fail(str(expected), str(actual))
	
	assertEqualsInt = clone_function("assertEqualsInt", _assertEquals)
	assertEqualsStr = clone_function("assertEqualsStr", _assertEquals)
	assertEqualsBool = clone_function("assertEqualsBool", _assertEquals)
	
	def report_success(self):
		print "Test ", self.testCounter, " OK"
	
	def report_fail(self, expected, actual):
		print "Test ", self.testCounter, " FAIL: expected=", expected, " actual=", actual
	
	def message(self, s):
		print s
	
	def run(self):
		print "Unexpected call of abstract method"
	
