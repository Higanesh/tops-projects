/*
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
*/

#include <stdio.h>

int main() {
    int n = 5;  // Number of rows for the pyramid (odd numbers only)
    int rows = (n * 2) - 1;  // Calculate the number of rows in the pyramid

    for (int i = 1; i <= n; i++) {
        // Printing spaces before the stars
        for (int j = 1; j <= n - i; j++) {
            printf("  ");
        }
        // Printing stars
        for (int k = 1; k <= (2 * i - 1); k++) {
            printf("* ");
        }
        // Move to the next line
        printf("\n");
    }
    return 0;
}
