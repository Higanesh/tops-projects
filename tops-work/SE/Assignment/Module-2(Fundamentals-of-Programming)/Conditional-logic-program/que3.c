/*
Que3. WAP to check if the given year is a leap year or not.
*/

#include <stdio.h>

int main()
{
    int year;
    printf("Enter any year\n");
    scanf("%d",&year);
    if((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
    {
        printf("%d is the leap year",year);
    }
    else
    {
        printf("%d is not the leap year",year);
    }
    return 0;
}