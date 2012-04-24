
#include <stdlib.h>
#include <stdio.h>

#ifdef GCOL
        #include <gc.h>
        //#define GC_REDIRECT_TO_LOCAL
        //#include "gc_local_alloc.h"
#endif

#ifdef GCOL
        #define XMALLOC GC_MALLOC
        #define XFREE
#else
        #define XMALLOC malloc
        #define XFREE free
#endif


int* create_new_bucket(n) {
	int i;
	int *result =  (int*)XMALLOC(n*sizeof(int));

	for (i = 0; i < n; i++)
		result[i] = n;
	result[i / 2] = 123;
	return result;	
}

#ifndef SUMCHECK
#define SUMCHECK 0
#endif

#if SUMCHECK > 0
int sum_bucket(int * bucket, int len) {
	int i;
	int result = 0;
	for (i = 0; i < len; i++) {
		result += bucket[i];
	}
	return result;
}
#endif

#define HISTORY_SIZE 100
#define BUCKET_SIZES_LEN 3

int body_main(void) {
	int* history[HISTORY_SIZE];
	int history_sizes[HISTORY_SIZE];
	int n = 10000;
	int bucket_sizes[BUCKET_SIZES_LEN];
	int i, check;
#if SUMCHECK > 0
	int sum = 0;
#endif
#if SUMCHECK > 1
	int c = 0;
	int j;
#endif


	bucket_sizes[0] = 1;
	bucket_sizes[1] = 1000;
	bucket_sizes[2] = 100000;

	for (i = 0; i < HISTORY_SIZE; i++) {
		history[i] = NULL;
	}

	for (i = 0; i < n; i++) {
		int new_size = bucket_sizes[i % BUCKET_SIZES_LEN];
		int * new_bucket = create_new_bucket(new_size);
		XFREE(history[i % HISTORY_SIZE]);
		history[i % HISTORY_SIZE] = new_bucket;
		history_sizes[i % HISTORY_SIZE] = new_size;
#if SUMCHECK > 0
		sum += sum_bucket(new_bucket, new_size);
#endif
#if SUMCHECK > 1
		c++;
		if (c == HISTORY_SIZE) {
			for (j = 0; j < HISTORY_SIZE; j++)
				sum += sum_bucket(history[j], history_sizes[j]);
			c = 0;
		}
#endif
	}
	
	check = HISTORY_SIZE / 2;
	printf("%d\n%d\n%d\n", history_sizes[check], history_sizes[check+1], history_sizes[check+2]);
#if SUMCHECK > 0
	printf("Sumcheck %d\n", sum);
#endif
#if SUMCHECK > 1
	printf("Sumcheck > 1");
#endif

	return 0;
}
