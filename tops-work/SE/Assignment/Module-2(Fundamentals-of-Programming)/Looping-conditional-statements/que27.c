/*
Que27. 1 2 3 6 9 18 27 54...
*/

#include <stdio.h>

int main() {
    int n, current = 1;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    
    // Print the first term
    printf("%d ", current);

    for(int i = 1; i < n; i++) {
        if(i % 3 == 1) {
            current *= 2;
        } else if(i % 3 == 2) {
            current *= 3;
        } else {
            current *= 1;
        }
        
        printf("%d ", current);
    }

    printf("\n");
    return 0;
}
