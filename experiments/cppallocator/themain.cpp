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

#include <cstdlib>
#include "creator.cpp"

int main(int argc, char* argv[]) {
	int n = 100000;
	int loops = 1000;
	int threads = 0;
	if (argc == 4) {
		n = atoi(argv[1]);
		loops = atoi(argv[2]);
		threads = atoi(argv[3]);
	}
	Creator * c = new Creator(n, loops);
	c->body();
	return 0;
}
