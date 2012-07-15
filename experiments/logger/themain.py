
from parlib.rtime import sleep
from parlib.directive import POSIX

from database import Database
from summarizer import Summarizer
from clock import Clock
from driver import Driver
from alarmwriter import AlarmWriter
from alarmlog import AlarmLog


def main():
	database = Database()
	alarmLog = AlarmLog()
	summarizer = Summarizer(database, alarmLog)
	clock = Clock(summarizer)
	alarmWriter = AlarmWriter(summarizer)
	driver1 = Driver(1, summarizer)
	
	clock.start()
	alarmWriter.start()
	driver1.start()
	sleep(1000)

if __name__=="__main__":
	main()

def entry_point(argv):
	if POSIX:
		from parlib.rthreading import init_threads
		init_threads()
	main()
	return 0

def target(*args):
	return entry_point, None
