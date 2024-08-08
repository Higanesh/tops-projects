/*
Que32. Accept 2 numbers and find out its sum check it size
*/

#include <stdio.h>

void main() {

   int num1,num2,sum;
   printf("Enter two numbers for sum\n");
   scanf("%d%d",&num1,&num2);
   sum = num1 + num2;
   printf("Sum of %d & %d is equal to %d\n",num1,num2,sum);
   printf("Size of variable sum is %d",sizeof(sum));
   
}