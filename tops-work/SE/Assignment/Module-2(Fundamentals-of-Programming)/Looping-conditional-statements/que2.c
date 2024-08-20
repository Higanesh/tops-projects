/*
Que2. WAP to accept 5 numbers from user and display all numbers
*/

#include <stdio.h>

int main()
{
    int array[5];
    printf("Enter 5 integer numbers\n");
    for(int i = 0; i < 5; i++)
    {
        scanf("%d",&array[i]);
    }
    printf("These are the 5 integer numbers\n");
    for(int i = 0; i < 5; i++)
    {
        printf("%d\n",array[i]);
    }
    return 0;
}