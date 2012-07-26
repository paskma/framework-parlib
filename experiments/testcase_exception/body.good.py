from parlib.rtime import sleep


from worker import Worker
from result import Result

def main(argv):
	result = Result()
	
	w1 = Worker(0.1, 100, result)
	w1.start()	
	w1.join()
	
	w2 = Worker(0.2, 200, result)
	w2.start()	
	w2.join()
	
	print result.get()
	print "Done."

