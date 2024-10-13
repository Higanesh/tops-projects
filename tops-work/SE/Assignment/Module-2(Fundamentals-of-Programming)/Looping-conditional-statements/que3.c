/*
Que3. WAP to take 10 no. Input from user find out below values
    a. How many Even numbers are there
    b. How many odd numbers are there
    c. Sum of even numbers
    d. Sum of odd numbers
*/

#include <stdio.h>

int main()
{
    int array[10];
    int even_counter = 0,odd_counter = 0,even_sum = 0,odd_sum = 0;
    printf("Enter 10 integer numbers\n");
    for(int i = 0; i < 10; i++)
    {
        scanf("%d",&array[i]);
    }
    for(int i = 0; i < 10; i++)
    {
        if(array[i] % 2 == 0)
        {
            even_counter++;
            even_sum += array[i];
        }
        else
        {
            odd_counter++;
            odd_sum += array[i];
        }
    }
    
    printf("Even numbers are %d\n",even_counter);
    printf("Odd numbers are %d\n",odd_counter);
    printf("Sum of even numbers are %d\n",even_sum);
    printf("Sum of odd numbers are %d\n",odd_sum);
    return 0;
}