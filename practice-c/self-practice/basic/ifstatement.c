#include<stdio.h>

void main()
{
    double bal = 34000,withdraw = 2000;
    printf("enter withdraw amount :\n");
    scanf("%.2f",&withdraw);
    if(bal > withdraw)
    {
        printf("money withdraw successfully : %.2f\nnow your remaining balance is : %.2f",withdraw,bal);
    }
}

