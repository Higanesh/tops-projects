/*
Que10. Write a program you have to make a summation of first and last Digit. (E.g.,1234 Ans: -5)
*/

#include <stdio.h>
#include <stdlib.h>
int main()
{
    int real_number,number,digit[20],i = 0,sum = 0;
    printf("Enter any number\n");
    scanf("%d",&real_number);
    number = abs(real_number);
    while(number > 0)
    {
        digit[i] = number % 10;
        number = number / 10;
        i++;
    }
    for(int j = 0; j <= i; j++)
    {
       sum = digit[0] + digit[i - 1];
    }
    printf("Sum of %d number is %d",real_number,sum);
    return 0;
}