/*
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
*/

#include <stdio.h>

int main() {
    int n = 5;  // Number of rows
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= i; j++) {
            printf("%d ", j % 2);  // Print 1 and 0 alternately
        }
        printf("\n");
    }
    return 0;
}