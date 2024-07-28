/*
Que2. Write a program to make Simple calculator (to make addition, subtraction, multiplication, division and modulo)
*/

#include <stdio.h>

void main() {
    
    int a,b;
    printf("Enter value of 'a' and 'b'\n");
    scanf("%d %d",&a,&b);
    printf("Addition of two numbers %d + %d = %d\n",a,b,a+b);
    printf("Subtraction of two numbers %d - %d = %d\n",a,b,a-b);
    printf("Multiplacation of two numbers %d * %d = %d\n",a,b,a*b);
    printf("Division of two numbers %d / %d = %d\n",a,b,a/b);
    printf("Modulo of two numbers %d %% %d = %d\n",a,b,a%b);

}