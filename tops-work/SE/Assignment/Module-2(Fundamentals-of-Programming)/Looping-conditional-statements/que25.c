/*
Que25. (1) + (1+2) + (1+2+3) + (1+2+3+4) + ... + (1+2+3+4+...+n)
*/

#include <stdio.h>

int main() {
    int n, total_sum = 0;

    // Input the number of terms
    printf("Enter the value of n: ");
    scanf("%d", &n);

    // Loop through each term in the series
    for(int i = 1; i <= n; i++) {
        // Calculate the sum of integers from 1 to i
        int sum = 0;
        for(int j = 1; j <= i; j++) {
            sum += j;
        }
        // Add this sum to the total sum
        total_sum += sum;
    }

    // Print the result
    printf("The result of the series is: %d\n", total_sum);

    return 0;
}

