
/*
class Item:
	def __init__(self, n, next):
		self.n = n
		self.next = next
*/

#ifdef GCOL
	#ifdef MT
		#define GC_THREADS
	#endif
	#include <gc.h>
	//#define GC_REDIRECT_TO_LOCAL
	//#include "gc_local_alloc.h"
#endif

#ifdef GCOL
	#define XMALLOC GC_MALLOC
#else
	#include <stdlib.h>
	#define XMALLOC malloc
#endif

#include "item.h"

struct Item * Item_init(int n, struct Item * next) {
	struct Item* result = XMALLOC(sizeof(struct Item));
	result->n = n;
	result->next = next;
	return result;
}
	
	
