/*
14] What is a recursive function? Write a C program to calculate the
factorial of a number using recursion.
*/

//Ans: A recursive function is a function that calls itself in order to solve a problem.

#include <stdio.h>

int factorial(int fact)
{
    if(fact == 1){
        return 1;
    }else{
        return fact * factorial( fact - 1);
    }
   
}
int main()
{
    int no;
    printf("Enter any no for calculate the factorial\n");
    scanf("%d",&no);
    printf("%d",factorial(no));
    
    return 0;
}