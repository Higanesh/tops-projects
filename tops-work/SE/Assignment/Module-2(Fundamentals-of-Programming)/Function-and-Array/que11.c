/*
Que11. WAP to accept 5 numbers from user and display in reverse order using for loop and array
*/

#include <stdio.h>

const int SIZE = 5;

int main() {
    int numbers[SIZE];
    
    printf("Enter %d numbers:\n", SIZE);
    for (int i = 0; i < SIZE; i++) {
        scanf("%d", &numbers[i]);
    }
    
    printf("Numbers in reverse order:\n");
    for (int i = SIZE - 1; i >= 0; i--) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    
    return 0;
}