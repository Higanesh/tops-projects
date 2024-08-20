/*
Que16. Calculate the Sum of Natural Numbers Using the While Loop
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
    int i = 0;
    while(i < size)
    {
        scanf("%d",&array[i]);
        sum += array[i];
        i++;
    }
    printf("Sum of %d array elements is %d",size,sum);
    return 0;
}