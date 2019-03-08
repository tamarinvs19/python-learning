#include <stdio.h>
#include <stdlib.h>

long* merge(long *x, long *y) {
    long i, j;
    long result[sizeof x + sizeof y];
    while (i < sizeof x && j < sizeof y){
	if (x[i] < y[j]) {
	    result[i+j] = x[i];
	    i++;
	}
	else {
	    result[i+j] = y[j];
	    j++;
	}
    }
    if (i < sizeof x) {
	while (j < sizeof y){
	    result[i+j] = y[j];
	    y++;
	}
    }
    else {
	while (i < sizeof x){
	    result[i+j] = x[i];
	    i++;
	}
    }
    printf(result);
    return result;
}

int main() {
    long *r;
    long a[3] = {1, 2, 3}, b[3] = {2, 3, 4};
    r = merge(a, b);
    printf( "\nYou entered: %ld ", r[0]);
    return 0;
}