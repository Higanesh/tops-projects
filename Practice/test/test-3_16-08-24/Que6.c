/*
6] Create a C program that calculates the sum and average of elements in an array.
*/

#include <stdio.h>

int main() {
    int len;
    int arr[5];
    int sum,avg;
    len = sizeof(arr) / sizeof(arr[0]);
    printf("Enter elements\n");
    for(int i = 0; i < len; i++)
    {
        scanf("%d",&arr[i]);
    }
    
    for(int i = 0; i < len; i++)
    {
        sum += arr[i];
    }
    avg = sum / len;
    printf("sum of array is %d\n",sum);
    printf("Average of array is %d",avg);
    return 0;
}