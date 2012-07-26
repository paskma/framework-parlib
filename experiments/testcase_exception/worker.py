from parlibutil.threading import Thread
from parlib.rtime import sleep

class Worker(Thread):

	def __init__(self, sleep_period, value, result):
		Thread.__init__(self)
		self.sleep_period = sleep_period
		self.value = value
		self.result = result
		
	def run(self, *args):
		sleep(self.sleep_period)
		self.result.put(self.value)
