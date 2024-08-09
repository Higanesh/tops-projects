/*
Que1. Write a C program to accept two integers and check whether they are equal or not
*/

#include <stdio.h>
#include <stdbool.h>

int main() {
    
    int num1,num2;
    bool flag = false;
    do{
        printf("Enter two numbers for comparison\n");
        printf("Enter first number\n");
        scanf("%d",&num1);
        printf("Enter second number\n");
        scanf("%d",&num2);
        if(num1 == num2)
        {
            printf("Both numbers are equal");
            flag = true;
        }
        else
        {
            printf("Both numbers are not equal\n");
        }

    }while(!flag);
    
    return 0;
}