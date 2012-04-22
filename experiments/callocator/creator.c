/*
from parlib.rthreading import Thread
from parlib.directive import POSIX
from item import Item
*/
#ifdef GCOL
	#ifdef MT
		#define GC_THREADS
		#define GC_LINUX_THREADS
		#define _REENTRANT
	#endif
	#include <gc.h>
	//#define GC_REDIRECT_TO_LOCAL
	//#include "gc_local_alloc.h"
#endif

#ifdef GCOL
	#define XMALLOC GC_MALLOC
#else
	#define XMALLOC malloc
#endif

#include <stdlib.h>
#include <stdio.h>
#include "item.h"

#ifdef MT
	#include <pthread.h>
#endif

#include "creator.h"

void log_impl(const char* s);
#define log log_impl
/*
class Creator(Thread):
	def __init__(self, n):
		if POSIX: Thread.__init__(self, Creator)
		self.n = n
		self.head = None
*/

struct Creator* Creator_init(int n, int loops) {
	struct Creator * result = XMALLOC(sizeof(struct Creator));
	result->n = n;
	result->head = NULL;
	result->loops = loops;
	return result;
}

/*
	def create(self):
		log("create")
		for i in range(0, self.n):
			log(str(i))
			current = Item(i, self.head)
			self.head = current
*/

void Creator_create(struct Creator* self) {
	int i;
	log("create");
	for (i = 0; i < self->n; i++) {
		struct Item * current = Item_init(i, self->head);
		self->head = current;
		//printf("create %d\n", i);
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

void Creator_hang(struct Creator* self) {
	log("hang");
	struct Item* current = self->head;
	int c = self->loops;
	while (c > 0) {
		current->n++;
		current = current->next;
		if (current == NULL) {
			//printf("%d\n", self->head->n);
			current = self->head;
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

void Creator_body(struct Creator* self) {
	log("body start");
	Creator_create(self);
	Creator_hang(self);
	log("body end");
}
/*	
	def RUN(self, *args):
		self.release_bootlock()
		self.body()
*/
#ifdef MT
void* Creator_run(void *creator) {
	Creator_body((struct Creator*)creator);
	return NULL;
}

long Creator_start(struct Creator* self) {
	int status = 0;
	pthread_t th;
	pthread_attr_t attrs;

	pthread_attr_init(&attrs);

	//printf("thread_start called\n");
	status = pthread_create(&th, &attrs, Creator_run, (void*)self);

	if (status != 0)
		    return -1;

	pthread_detach(th);

	return (long)th;
}
#endif

/*
def log(s):
	#print s
	pass
*/

#undef log
void log_impl(const char * s) {
	//printf("%s\n", s);
}
