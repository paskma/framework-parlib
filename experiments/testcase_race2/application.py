from parlib.rtime import sleep

from counter import Counter
from worker import Worker

class Application:
	def main(self, argv):
		n = 5
		if len(argv) >= 2:
			n = int(argv[1])

		counter = Counter()
		
		w1 = Worker(counter, n)
		w2 = Worker(counter, n)
	
		#print "Starting threads"
		w1.start()
		w2.start()
	
		w1.join()
		w2.join()
		print counter.getValue()
		print "Done."
		return 0

