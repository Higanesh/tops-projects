/*
Que19. Calculate compound interest
*/

#include <stdio.h>
#include <math.h>

int main() {
    
    double amount,principalAmt,interestRate,noOfTimes,time,compoundInterest;
    
    printf("Enter principal amount\n");
    scanf("%lf",&principalAmt);
    
    printf("Enter interest rate\n");
    scanf("%lf",&interestRate);
    
    printf("Enter number of times\n");
    scanf("%lf",&noOfTimes);
    
    printf("Enter time period\n");
    scanf("%lf",&time);
    
    amount = principalAmt * pow((1 + interestRate/noOfTimes),noOfTimes*time);
    compoundInterest = amount - principalAmt;
    printf("Compound interest : %.2lf",compoundInterest);
    
    return 0;
}