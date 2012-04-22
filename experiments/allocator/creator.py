from parlib.rthreading import Thread
from parlib.directive import POSIX
from item import Item

class Creator(Thread):
	def __init__(self, n, loops):
		if POSIX: Thread.__init__(self, Creator)
		self.n = n
		self.head = None
		self.loops = loops
	
	def create(self):
		log("create")
		for i in range(0, self.n):
			log(str(i))
			current = Item(i, self.head)
			self.head = current
	
	def hang(self):
		log("hang")
		current = self.head
		c = self.loops
		while c > 0:
			current.n += 1
			current = current.next
			if current is None:
				#print self.head.n
				current = self.head
				c -= 1
				
	def body(self):
		log("body start")
		self.create()
		#print self.head.n
		self.hang()
		log("body end")
	
	def RUN(self, *args):
		self.release_bootlock()
		self.body()

def log(s):
	#print s
	pass
