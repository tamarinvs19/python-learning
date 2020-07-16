#include <stdio.h>
#include <stdlib.h>

void merge(int x[], int y[], size_t size_x, size_t size_y, int result[]) {
    int i = 0;
    int j = 0;
    while ((i < size_x) && (j < size_y)){
	printf("%d %d\n", i, j);
	if (x[i] <= y[j]) {
	    result[i+j] = x[i];
	    i++;
	}
	else {
	    result[i+j] = y[j];
	    j++;
	}
    }
    while (i < size_x){
	result[i+j] = x[i];
	i++;
    }
    while (j < size_y){
	result[i+j] = y[j];
	j++;
    }
}

int main() {
    int a[3] = {1, 2, 10};
    int b[4] = {2, 3, 9, 50};
    int *r = (int *)calloc(7*sizeof(int), 0);
    merge(a, b, 3, 4, r);
    for (int i = 0; i < 7; i++)
	printf("%d ", r[i]);
    free(r);
    return 0;
}
