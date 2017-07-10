#include <stdio.h>
#include <time.h>

double rand_array(int sz) {
	double x[sz];
	for (int i = 0; i < sz; i++) {
	        n = (double)rand()/RAND_MAX;
		x[i] = n;
	}
	return x;
}

int main(int argc, char *argv[]) {
	int n = 100000;
	double p = 0.1;
	double q = 0.2;
	double U[] = rand_array(n);
	double x[n]
	x[0] = 1
	for (int i = 1; i < n; i++) {
		x_curr = x[i-1];
		double step = U[i];
		if (x_curr == 0) {
			x[i] = (step < p);
		else x[i] = (step > q);
	return x;
}

