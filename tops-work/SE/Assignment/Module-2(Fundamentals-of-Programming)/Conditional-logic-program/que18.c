/*
Que18. Write a C program to calculate profit and loss on a transaction.
*/

#include <stdio.h>

int main()
{
    float cost_price,sale_price,profit,loss;
    printf("Enter your cost price\n");
    scanf("%f",&cost_price);
    
    printf("Enter your sale price\n");
    scanf("%f",&sale_price);
    
    if(cost_price < sale_price)
    {
        profit = sale_price - cost_price;
        printf("The total profit on transaction is: %.2f\n",profit);
    }
    else if(cost_price > sale_price)
     {
        loss = cost_price - sale_price;
        printf("The total loss on transaction is: %.2f\n",loss);
    }
    else
    {
        printf("There is no profit, no loss. Bought and sold at the same price\n");
    }
    return 0;
}
