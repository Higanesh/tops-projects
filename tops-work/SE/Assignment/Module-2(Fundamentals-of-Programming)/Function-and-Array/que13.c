/*
Que13. WAP to accept 5 numbers from user and check entered number is even or odd using of array
*/

#include <stdio.h>

int main()
{
    int array[5];
    int even_counter = 0,odd_counter = 0;
    printf("Enter 5 integer numbers\n");
    int i = 0;
    while(i < 5)
    {
        scanf("%d",&array[i]);
        i++;
    }
    int j = 0;
    while(j < 5)
    {
        if(array[j] % 2 == 0)
        {
            even_counter++;
        }
        else
        {
            odd_counter++;
        }
        j++;
    }
    
    printf("Even numbers are %d\n",even_counter);
    printf("Odd numbers are %d\n",odd_counter);
    
    return 0;
}