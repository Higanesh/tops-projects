/*
18] Write a C program to check if a given number is even or odd using the modulo
operator.
*/

#include <stdio.h>

int main() {
    
    int no;
    printf("Enter any number\n");
    scanf("%d",&no);
    if(no % 2 == 0)
    {
        printf("%d Number is EVEN",no);
    }
    else
    {
        printf("%d Number is ODD",no);
    }
    
    return 0;
}