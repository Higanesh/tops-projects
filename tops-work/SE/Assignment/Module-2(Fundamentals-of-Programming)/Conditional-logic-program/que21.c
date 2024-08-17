/*
Que21. Write a program in C to read any Month Number in integer and display the number of days for this month.
*/

#include <stdio.h>

int main() {
    
    int month_no;
    printf("Enter month number\n");
    scanf("%d",&month_no);
    switch(month_no)
    {
        case 1:case 3: case 5: case 7: case 8:case 10: case 12: printf("31 days");
        break;
        case 4: case 6: case 9: case 11: printf("30 days");
        break;
        case 2: printf("28 or 29 days");
        break;
        default: printf("INVALID month number");
        break;
    }
    return 0;
}