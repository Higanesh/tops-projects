/*
Que5. WAP to print factorial of given number
*/

#include <stdio.h>

int factorial(int fact)
{
    if(fact == 1){
        return 1;
    }else{
        return fact * factorial(fact - 1);
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