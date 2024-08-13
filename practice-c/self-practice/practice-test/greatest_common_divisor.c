/*
Que20. Write a C program that uses a recursive function to find the
Greatest Common Divisor (GCD) of two numbers.
*/

/*
10] Write a function in C that takes an array of integers and its size
as input and returns the sum of all elements in the array.
*/

#include <stdio.h>

int main()
{
    int first_no[3],second_no[20],common_factors[20];
    int no1,no2,temp=1,len1,len2;
    printf("Enter any two numbers\n");
    scanf("%d",&no1);
    for(int i = 1; i < no1; i++)
    {
        if(no1 % i == 0)
        {
            first_no[i-1] = i;
        }
    }
    len1 = sizeof(first_no)/sizeof(first_no[0]);
    printf("%d\n",len1);
    for(int j = 0; j < len1; j++)
    {
        printf("%d ",first_no[j]);
    }
    printf("\n");
    
    return 0;
}