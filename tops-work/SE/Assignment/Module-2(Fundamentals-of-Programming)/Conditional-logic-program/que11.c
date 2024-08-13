/*
Que11. WAP to find number is even or odd using ternary operator
*/

#include <stdio.h>

int main()
{
    int no;
    printf("Enter any number\n");
    scanf("%d",&no);
    no % 2 == 0 ? printf("Number is EVEN") : printf("Number is ODD");
    return 0;
}