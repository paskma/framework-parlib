from resource import Resource
from worker import Worker

class Application:
	def main(self, argv):
		res1 = Resource()
		res2 = Resource()
		res1.setSecondLevel(res2)
		res2.setSecondLevel(res1)

		w1 = Worker(res1)
		w2 = Worker(res1)

		w1.start()
		w2.start()
		
		w1.join()
		w2.join()
		return 0
