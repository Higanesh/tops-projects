/*
Que26. 1/2 - 2/3 + 3/4 - 4/5 + 5/6 .......... n
*/

#include <stdio.h>

int main() {
    int n;
    double sum = 0.0;

    // Input the number of terms
    printf("Enter the number of terms (n): ");
    scanf("%d", &n);

    // Loop through the series and calculate the sum
    for(int i = 1; i <= n; i++) {
        // Alternate sign based on whether i is odd or even
        if(i % 2 == 1) {
            sum += (double)i / (i + 1);  // Add for odd i
        } else {
            sum -= (double)i / (i + 1);  // Subtract for even i
        }
    }

    // Print the result
    printf("The result of the series is: %lf\n", sum);

    return 0;
}
