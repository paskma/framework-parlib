/*
from parlib.rtime import sleep
from parlib.directive import POSIX

from creator import Creator

def main():
	c = Creator(100000)
	#c.start()
	#sleep(1000)
	c.body()

if __name__ == "__main__":
	main()

def entry_point(args):
	if POSIX:
		from parlib.rthreading import init_threads
		init_threads()
	main()
	return 0

def target(*args):
	return entry_point, None
*/
#include <time.h>
#include <errno.h>
#include <signal.h>
#include <stdio.h>


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
#include "creator.h"

void sig_ignore(int signum)
{
    struct sigaction context;
    context.sa_handler = SIG_IGN;
    sigemptyset(&context.sa_mask);
    context.sa_flags = 0;
    sigaction(signum, &context, NULL);
}

#ifdef MT
void d_sleep(double secs) {
	struct timespec amount;
	int suc;
	int integer;
	double part;
	//int counter = 0;
	
	integer = (int)secs;
	part = (secs - integer) * 1000000000.0;
	
	amount.tv_sec = (time_t)integer;
	amount.tv_nsec = (long)part;
	for(;;) {
		//printf("sleep #%d\n", counter++);
		suc = nanosleep(&amount, &amount);
		if (suc == 0)
			break;
		else {
			if (errno = EINTR)
				continue; /* interrupted, can try again */
			else
				break; /* callee does not know about failure */
		}
	}
}
#endif /* defined MT */

int main(int argc, char* argv[]) {
	int n = 100000;
	int loops = 1000;
	int threads = 0;
#ifdef GCOL
	GC_INIT();
#endif
	if (argc == 4) {
		n = atoi(argv[1]);
		loops = atoi(argv[2]);
		threads = atoi(argv[3]);
	}
	struct Creator * c = Creator_init(n, loops);
#ifdef MT
	if (threads == 1) {
		Creator_start(c);
		//sig_ignore(30);
		d_sleep(1000);
	} else {
		Creator_body(c);
	}
#else
	Creator_body(c);
#endif
	return 0;
}
