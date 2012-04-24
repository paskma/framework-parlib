/*
from parlib.rthreading import Thread
from parlib.directive import POSIX
from item import Item
*/
#include <iostream>
#include "item.cpp"

void log_impl(const char* s);
#define log log_impl
/*
class Creator(Thread):
	def __init__(self, n):
		if POSIX: Thread.__init__(self, Creator)
		self.n = n
		self.head = None
*/
class Creator {
public:
	int n;
	Item * head;
	int loops;
	Creator(int n, int loops);
	virtual void create();
	virtual void hang();
	virtual void body();
};

Creator::Creator(int n, int loops) {
	this->n = n;
	this->head = NULL;
	this->loops = loops;
}

/*
	def create(self):
		log("create")
		for i in range(0, self.n):
			log(str(i))
			current = Item(i, self.head)
			self.head = current
*/

void Creator::create() {
	int i;
	log("create");
	for (i = 0; i < this->n; i++) {
		Item * current = new Item(i, this->head);
		this->head = current;
	}
}


/*	
	def hang(self):
		log("hang")
		current = self.head
		c = 100000
		while c > 0:
			current.n += 1
			current = current.next
			if current is None:
				#print self.head.n
				current = self.head
				c -= 1
*/

void Creator::hang() {
	log("hang");
	Item* current = this->head;
	int c = this->loops;
	while (c > 0) {
		current->n++;
		current = current->next;
		if (current == NULL) {
			//printf("%d\n", self->head->n);
			current = this->head;
			c--;
		}
	}
}

/*				
	def body(self):
		log("body start")
		self.create()
		#print self.head.n
		self.hang()
		log("body end")
*/

void Creator::body() {
	log("body start");
	create();
	hang();
	log("body end");
}
/*	
	def RUN(self, *args):
		self.release_bootlock()
		self.body()
*/
/*
def log(s):
	#print s
	pass
*/

#undef log
void log_impl(const char * s) {
	//std::cout << s << std::endl;
}
