/*
13] Write a C program to find the smallest element in an array of integers.
*/

#include <stdio.h>

int main() {
    
    int no_array[20];
    int temp,len;
    printf("Enter length of array\n");
    scanf("%d",&len);
    for(int i = 0; i < len; i++)
    {
        scanf("%d",&no_array[i]);
    }
    //int len = sizeof(no_array)/sizeof(no_array[0]);
    for(int i = 0; i < len - 1; i++)
    {
        for(int j = 0; j < len - i - 1; j++)
        {
            if(no_array[j] < no_array[j+1])
            {
                temp = no_array[j+1];
                no_array[j+1] = no_array[j];
                no_array[j] = temp;
            }
        }
    }
    printf("Smallest number is %d",no_array[len-1]);
    

    return 0;
}