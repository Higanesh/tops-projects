/*
16] Write a C program to find the largest element in an array of
integers.
*/

#include <stdio.h>

int main() {
    
    int array[20];
    int temp,size;
    printf("Enter no. of elements\n");
    scanf("%d",&size);
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
    printf("Largest no. is %d",array[size-1]);
    return 0;
}