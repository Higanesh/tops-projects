/*
Que13. calculate the Factorial of a Given Number using while loop
*/

#include <stdio.h>

int main()
{
    int no,fact = 1;
    printf("Enter any no for calculate the factorial\n");
    scanf("%d",&no);
    while(no > 0)
    {
        fact = fact * no;
        no--;
    }
    printf("%d",fact);
    
    return 0;
}