#include<stdio.h>

void main()
{
    double bal = 34000,withdraw = 200000;
   
    if(bal > withdraw)
    {
        printf("money withdraw successfully : %.2f\nnow your remaining balance is : %.2f",withdraw,bal);
    }
    else
    {
        printf("insufficient balance");
    }
}