/*
18] Create a C program that checks if a given year is a leap year.
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