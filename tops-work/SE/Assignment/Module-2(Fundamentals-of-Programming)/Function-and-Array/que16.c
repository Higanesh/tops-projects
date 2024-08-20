/*
Que16. Accept 5 numbers from user and perform sum of array
*/

#include <stdio.h>

int main()
{
    int size = 5;
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