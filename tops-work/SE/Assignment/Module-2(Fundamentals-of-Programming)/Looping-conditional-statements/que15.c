/*
Que15. Calculate sum of 10 numbers using of while loop
*/

#include <stdio.h>

int main()
{
    int size = 10;
    int array[size];
    int sum = 0;
    printf("Enter %d elements in array for sum\n",size);
    int i = 0;
    while(i < size)
    {
        scanf("%d",&array[i]);
        i++;
    }
    int j = 0;
    while(j < size)
    {
        sum += array[j];
        j++;
    }
    printf("Sum of %d array elements is %d",size,sum);
    
    return 0;
}