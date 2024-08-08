/*
Que33. C Program to Read Integer and Print First Three Powers (N^1, N^2, N^3)
*/

#include <stdio.h>
#include <math.h>

void main() {

   int num;
   printf("Enter any integer number\n");
   scanf("%d",&num);
   printf("%d^1 = %.2lf\n",num,pow(num,1));
   printf("%d^2 = %.2lf\n",num,pow(num,2));
   printf("%d^3 = %.2lf",num,pow(num,3));
   
}