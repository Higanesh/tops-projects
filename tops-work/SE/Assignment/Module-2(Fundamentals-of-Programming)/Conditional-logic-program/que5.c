/*
Que5. Check Number Is Positive or Negative
*/

#include <stdio.h>

int main()
{
    int no;
    printf("Enter any integer number\n");
    scanf("%d",&no);
    if(no > 0)
    {
        printf("%d number is POSITIVE",no);
    }
    else if(no < 0)
    {
        printf("%d number is NEGATIVE",no);
    }
    else
    {
        printf("%d number is ZERO",no);
    }
    return 0;
}