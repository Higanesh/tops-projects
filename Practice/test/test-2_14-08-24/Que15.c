/*
15] Write a C program that uses a for loop to calculate the sum of the first 10 natural
numbers.
*/

#include <stdio.h>

int main() {
    
    int no = 10,sum = 0;
    int no_array[no];
    printf("Enter first 10 natural numbers\n");
    for(int i = 0; i < no; i++)
    {
        scanf("%d",&no_array[i]);
        sum += no_array[i];
    }
    printf("Sum of first 10 natural numbers is %d",sum);
    return 0;
}