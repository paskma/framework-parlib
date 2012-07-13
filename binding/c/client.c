#include <stdio.h>
//#include <signal.h>
#include "pasys.h"

void in_thread(void)
{
	printf("in_thread called\n");
}

void my_busy_wait(int n)
{
	dump("waiting...");
	int i;
	for (i = 0; i < n; i++)
		;
	printf(" finished.\n");
}


int main()
{
	int a,b,c;
	a = 1;
	b = 100;
	c = mean(a,b);
	int foo;
	LOCK* lock;
	printf("Mean is %d\n", c);
	printf("Sin test %f\n", pasys_sin(3.1/2.0)); // my approx of pi :-)
	thread_start(in_thread);
	thread_start(in_thread);
	//my_busy_wait(100000000);
	foo = busy_wait(10000);
	printf("foo %d\n", foo);
	lock = allocate_lock();
	acquire_lock(lock);
	printf("lock acquired\n");
	release_lock(lock);
	pasys_sleep(2.2);
	sig_ignore(30/*sigpwr*/);
	printf("Done.\n");
	return 0;
}
