/*
Que23. 1 + 2 + 3 + 4 + 5 + ... + n
*/

#include <stdio.h>

int main() {
    int n, total_sum = 0;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) {
        total_sum += i;
    }
    printf("The sum of the first %d natural numbers is: %d\n", n, total_sum);

    return 0;
}
