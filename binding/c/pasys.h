#ifndef __pasys_h__
#define __pasys_h__
int mean(int a, int b);
long thread_start(void (*func)(void));
int dump(const char* str);
int busy_wait(int n);


struct PRIV_LOCK;

typedef struct PRIV_LOCK LOCK;

LOCK* allocate_lock();
int acquire_lock(LOCK* lock);
int release_lock(LOCK* lock);

void sig_ignore(int signum);

int pasys_sleep(double seconds);
double pasys_sin(double angle);
#endif
