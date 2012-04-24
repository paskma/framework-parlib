#include <stdio.h>
#include <math.h>

double computation_poly(void) {
	double result = 0.0;
	double delta = 1e-9;
	double start = 0.0;
	double stop = 1.0;
	double x = start;
	double y;
	while (x <= stop) {
		y = (x * x + 7.0 * x + 1) / 3.0;
		result += delta * y;
		x += delta;
	}
	return result;
}

double computation_sin(void) {
	double result = 0.0;
	double delta = 1e-8;
	double start = 0.0;
	double stop = M_PI / 2.0;
	double x = start;
	double y;
	while (x <= stop) {
		y = sin(x);
		result += delta * y;
		x += delta;
	}
	return result;
}


int main(int argc, char *argv[]) {
	int n = 0;
	double x = -1;
	if (argc == 2) {
		n = atoi(argv[1]);
	}
	if (n == 0)
		x = computation_poly();
	else if (n == 1)
		x = computation_sin();
		
	printf("%d %f\n", n, x);
}
