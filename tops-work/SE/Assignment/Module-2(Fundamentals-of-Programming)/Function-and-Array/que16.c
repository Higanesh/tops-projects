/*
Que16. Accept 5 numbers from user and perform sum of array
*/

#include <stdio.h>

int main()
{
    int array[5];
    int sum = 0;
    printf("Enter %d elements in array for sum\n",5);
    int i = 0;
    while(i < 5)
    {
        scanf("%d",&array[i]);
        i++;
    }
    int j = 0;
    while(j < 5)
    {
        sum += array[j];
        j++;
    }
    printf("Sum of 5 array elements is %d",sum);
    
    return 0;
}