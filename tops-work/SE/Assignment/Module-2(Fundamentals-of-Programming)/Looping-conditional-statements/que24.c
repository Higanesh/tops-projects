/*
Que24. (1*1) + (2*2) + (3*3) + (4*4) + (5*5) + ... + (n*n)
*/

#include <stdio.h>

int main() {
    int n, total_sum = 0;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        total_sum += i * i;
    }
    printf("The sum of squares from 1 to %d is: %d\n", n, total_sum);
    return 0;
}
