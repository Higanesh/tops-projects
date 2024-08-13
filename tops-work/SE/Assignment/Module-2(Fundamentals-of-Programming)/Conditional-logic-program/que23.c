/*
Que23. WAP to input the week number and print week day.
*/

#include <stdio.h>

int main()
{
    int day_no;
    printf("Enter day number\n");
    scanf("%d",&day_no);
    switch(day_no)
        {
            case 1:printf("MONDAY");
            break;
            case 2:printf("TUESDAY");
            break;
            case 3:printf("WEDNESDAY");
            break;
            case 4:printf("THURSDAY");
            break;
            case 5:printf("FRIDAY");
            break;
            case 6:printf("SATURDAY");
            break;
            case 7:printf("SUNDAY");
            break;
            default:printf("INVALID DAY NUMBER\nEnter day number between 1 to 7");
            break;
        }
    return 0;
}