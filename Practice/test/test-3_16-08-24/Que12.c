/*
12] Write a C program to find the factorial of a number using both iterative and recursive
approaches.
*/

#include <stdio.h>

int iterative_factorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int recursive_factorial(int fact)
{
    if(fact == 1){
        return 1;
    }else{
        return fact * recursive_factorial(fact - 1);
    }
   
}
int main()
{
    int no;
    printf("Enter any no for calculate the factorial\n");
    scanf("%d",&no);
    printf("Factorial by iterative function %d\n",iterative_factorial(no));
    printf("Factorial by recursive function %d",recursive_factorial(no));
    return 0;
}