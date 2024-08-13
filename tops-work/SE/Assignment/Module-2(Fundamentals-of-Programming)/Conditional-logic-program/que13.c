/*
Que13. WAP to find minimum number among 3 numbers using ternary operator
*/

#include <stdio.h>

int main()
{
    int no1,no2,no3;
    printf("Enter any 3 numbers for comparison\n");
    scanf("%d%d%d",&no1,&no2,&no3);
    printf("%d %d %d\n",no1,no2,no3);
    no1 < no2 && no1 < no3 ? printf("%d is lesser",no1) : no2 < no1 && no2 < no3 ? printf("%d is lesser",no2) : printf("%d is lesser",no3); 
    return 0;
}