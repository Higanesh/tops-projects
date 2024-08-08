#include<stdio.h>
int sum=100;
void main()
{
   extern int sum;
   printf("sum is : %d\n",sum);
}

 int myfun1(int a, int b)
    {
        sum = a+b;
        return sum;
    }