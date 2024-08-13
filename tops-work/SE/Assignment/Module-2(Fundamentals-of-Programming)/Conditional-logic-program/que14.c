/*
Que14. WAP to find the largest of three numbers.
*/

#include <stdio.h>

int main()
{
    int no1,no2,no3;
    printf("Enter any 3 numbers for comparison\n");
    scanf("%d%d%d",&no1,&no2,&no3);
    printf("%d %d %d\n",no1,no2,no3);
    int max = no1 > no2 ? no1 > no3 ? no1 : no3 : no2 > no3 ? no2 : no3;
    printf("%d is greater",max);
    return 0;
}