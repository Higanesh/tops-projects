/*
Que6. WAP to print Fibonacci series up to given numbers
*/

#include <stdio.h>

int main() {
    int n, t1 = 0, t2 = 1, nextTerm = 0;

    // Input the number of terms
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: %d, %d", t1, t2);

    for (int i = 3; i <= n; ++i) {
        nextTerm = t1 + t2;
        printf(", %d", nextTerm);
        t1 = t2;
        t2 = nextTerm;
    }

    return 0;
}
