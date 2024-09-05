/*
Que25. (1) + (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n)
*/

#include <stdio.h>

int main() {
    int n, total_sum = 0;

    printf("Enter the value of n: ");
    scanf("%d", &n);

    for(int i = 1; i <= n; i++) {
        int sum = 0;
        for(int j = 1; j <= i; j++) {
            sum += j;
        }
        total_sum += sum;
    }
    printf("The result of the series is: %d\n", total_sum);

    return 0;
}

