

struct Creator {
	int n;
	struct Item * head;
	int loops;
};

struct Creator* Creator_init(int n, int loops);
void Creator_create(struct Creator* self);
void Creator_hang(struct Creator* self);
void Creator_body(struct Creator* self);
#ifdef MT
void* Creator_run(void *creator);
long Creator_start(struct Creator* self);
#endif
