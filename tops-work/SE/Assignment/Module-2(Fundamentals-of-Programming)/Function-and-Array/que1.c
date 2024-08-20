/*
Que1. Write a program to find out the max number from given array using function
*/

#include <stdio.h>

int find_max(int size)
{
    int temp;
    int array[20];
    printf("Enter array elements\n");
    for(int i = 0; i < size; i++)
    {
         scanf("%d",&array[i]);
    }
    for(int j = 0; j < size - 1; j++)
    {
        if(array[j] > array[j+1])
        {
            temp = array[j];
            array[j] = array[j+1];
            array[j+1] = temp;
        }
    }
    return array[size - 1];
}

int main()
{
    int size;
    printf("Enter no. of elements\n");
    scanf("%d",&size);
    printf("Largest no. is %d",find_max(size));
    return 0;
}