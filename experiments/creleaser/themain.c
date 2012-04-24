#include <stdio.h>


#ifdef GCOL
	#include <gc.h>
	//#define GC_REDIRECT_TO_LOCAL
	//#include "gc_local_alloc.h"
#endif
#include "body.h"


int main(int argc, char* argv[]) {
#ifdef GCOL
	GC_INIT();
#endif
	return body_main();
}
