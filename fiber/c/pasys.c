#include "pasys.h"
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <signal.h>
#include <sys/select.h>
#include <time.h>
#include <errno.h>
#include <math.h>

int mean(int a, int b)
{
	return (a+b)/2;
}

int dump(const char* str)
{
	printf("%s", str);
	fflush(stdout);
	return 0;
}

int busy_wait(int n)
{
	int M = 10000;
	int foo = 0, bar = 0;
	int i,j;
	for(i=0;i<n;i++)
	{
		bar = 0;
		for(j=0;j<M;j++)
			bar += j;
		foo += bar - M*(M-1)/2 + 1;
	}
	return foo;
}

static void *bootstrap_pthread(void *func)
{
	//printf("bootstrap executed %x\n", func);
 	((void(*)(void))func)();
 	//printf("bootstrap end\n");
	return NULL;
}

long thread_start(void (*func)(void))
{
	int status = 0;
	pthread_t th;
	pthread_attr_t attrs;
	
	pthread_attr_init(&attrs);
	
	//printf("thread_start called\n");
	status = pthread_create(&th, &attrs, bootstrap_pthread, (void*)func);
	
	if (status != 0)
		return -1;
	
	pthread_detach(th);
	
	return (long)th;
}

struct PRIV_LOCK
{
	pthread_mutex_t mutex;
};


LOCK* allocate_lock()
{
	LOCK *result = (LOCK*)malloc(sizeof(LOCK));
	int suc = pthread_mutex_init(&result->mutex, NULL);
	assert(!suc);
	return result;
}

int acquire_lock(LOCK* lock)
{
	int suc = pthread_mutex_lock(&lock->mutex);
	assert(!suc);
	return suc;
}

int release_lock(LOCK* lock)
{
	int suc = pthread_mutex_unlock(&lock->mutex);
	assert(!suc);
	return suc;
}

void sig_ignore(int signum)
{
    struct sigaction context;
    context.sa_handler = SIG_IGN;
    sigemptyset(&context.sa_mask);
    context.sa_flags = 0;
    sigaction(signum, &context, NULL);
}

/**
	Sleep that may be interrupted.
*/
int pasys_sleep_intr(double seconds)
{
	struct timeval t;
	int secs = (int)seconds;
	int frac = (int)(seconds - secs);
	t.tv_sec = secs;
	t.tv_usec = frac*1000000;
	return select(0, NULL, NULL, NULL, &t);
}

/**
	Sleep with safety loop.
*/
int pasys_sleep(double secs) {
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
				return -1;
		}
	}
	return 0;
}

/**
	Attempt to faster Sinus
*/
double pasys_sin(double angle) {
	return sin(angle);
}
