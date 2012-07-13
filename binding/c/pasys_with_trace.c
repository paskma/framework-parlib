#include "pasys.h"
#include <pthread.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <signal.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/select.h>

int mean(int a, int b)
{
	return (a+b)/2;
}

int dump(const char* str)
{
	int fd = open("/tmp/pasys.log", O_CREAT | O_WRONLY | O_APPEND, 0777);
	write(fd, str, strlen(str));
	return 0;
	close(fd);
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
	dump("PASYS:thread_start called\n");
	
	pthread_attr_init(&attrs);
	
	//printf("thread_start called\n");
	status = pthread_create(&th, &attrs, bootstrap_pthread, (void*)func);
	
	if (status != 0) {
		dump("PASYS:thread error\n");
		return -1;
	}
	
	pthread_detach(th);
	
	dump("PASYS:thread_start finish\n");
	return (long)th;
}

struct PRIV_LOCK
{
	pthread_mutex_t mutex;
};


LOCK* allocate_lock()
{
	dump("PASYS:allocate_lock\n");
	LOCK *result = (LOCK*)malloc(sizeof(LOCK));
	int suc = pthread_mutex_init(&result->mutex, NULL);
	assert(!suc);
	return result;
}

int acquire_lock(LOCK* lock)
{
	dump("PASYS:acquire_lock\n");
	int suc = pthread_mutex_lock(&lock->mutex);
	assert(!suc);
	return suc;
}

int release_lock(LOCK* lock)
{
	dump("PASYS:release_log\n");
	int suc = pthread_mutex_unlock(&lock->mutex);
	assert(!suc);
	return suc;
}

void sig_ignore(int signum)
{
	dump("PASYS:sig_ignore\n");
    struct sigaction context;
    context.sa_handler = SIG_IGN;
    sigemptyset(&context.sa_mask);
    context.sa_flags = 0;
    sigaction(signum, &context, NULL);
}

int pasys_sleep(double seconds)
{
	dump("PASYS:sleep\n");
	struct timeval t;
	int secs = (int)seconds;
	int frac = (int)(seconds - secs);
	t.tv_sec = secs;
	t.tv_usec = frac*1000000;
	return select(0, NULL, NULL, NULL, &t);
}
