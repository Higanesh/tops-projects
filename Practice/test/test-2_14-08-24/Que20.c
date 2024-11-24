/*
20 Write a C program that uses a recursive function to calculate the Fibonacci sequence
up to n terms.
*/

#include <stdio.h>

// Recursive function to calculate Fibonacci sequence
int fibonacci(int n) {
    if(n == 0) 
        return 0;
    else if(n == 1) 
        return 1;
    else 
        return (fibonacci(n - 1) + fibonacci(n - 2));
}

int main() {
    int n, i;

    // Input number of terms
    printf("Enter the number of terms: ");
    scanf("%d", &n);

    // Print Fibonacci sequence up to n terms
    printf("Fibonacci sequence up to %d terms:\n", n);
    for(i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    return 0;
}
