from parlib.verify import random

class Application:
	def main(self, argv):
		low_bit = random(1)
		high_bit = random(1)
		
		result = (high_bit << 1) | low_bit
		
		assert result != 0 #wrong assumption 
		
		print result	
		return 0
