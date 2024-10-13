/*
Que7. WAP to print number in reverse order e.g.: number = 64728 ---> reverse = 82746
*/

#include <stdio.h>

int main()
{
    int number,reverse,temp;
    printf("Enter any number\n");
    scanf("%d",&number);
    printf("Real number is %d\n",number);
    if(number <= 9)
    {
        reverse = number;
    }
    else
    {
        while(number > 0)
        {
            temp = number % 10;
            number = number / 10;
            reverse = (reverse * 10) + temp;
        }
    }
    printf("Reverse number is %d\n",reverse);
    return 0;
}