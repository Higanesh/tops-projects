/*
Que8. Write a program to find out the max from given number (E.g., No: -1562 Max number is 6)
*/

#include <stdio.h>

int main()
{
    int real_number,number,digit[20],i = 0,len,temp;
    printf("Enter any number\n");
    scanf("%d",&real_number);
    number = abs(real_number);
    while(number > 0)
    {
        digit[i] = number % 10;
        number = number / 10;
        i++;
    }
    temp = digit[0];
    for(int j = 1; j < i; j++)
    {
        if(temp < digit[j])
        {
            temp = digit[j];
        }
    }
    printf("Max from given number is %d",temp);
    return 0;
}