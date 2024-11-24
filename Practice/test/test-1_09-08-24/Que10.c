/*
10] Write a function in C that takes an array of integers and its size
as input and returns the sum of all elements in the array.
*/

#include <stdio.h>

int main()
{
    int size;
    int array[50];
    int sum = 0;
    printf("Enter size of an array\n");
    scanf("%d",&size);
    printf("Enter %d elements in array for sum\n",size);
    for(int i = 0; i < size; i++)
    {
        scanf("%d",&array[i]);
    }
    for(int j = 0; j < size; j++)
    {
        sum += array[j];
    }
    printf("Sum of all array elements is %d",sum);
    return 0;
}