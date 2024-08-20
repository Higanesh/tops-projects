/*
3] Write a C program to calculate the sum of the digits of an integer number entered by the user.
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
       sum += digit[j];
    }
    printf("Sum of %d number is %d",real_number,sum);
   
    return 0;
}
