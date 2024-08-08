/*
Que22. Calculate compound interest (Compound Interest formula:
a.
Formula to calculate compound interest annually is given by:
Amount= P(1 + R/100)t
b.
Compound Interest = Amount – P
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
    printf("Total amount is %.2lf",amount);
    compoundInterest = amount - principalAmt;
    printf("Compound interest : %.2lf",compoundInterest);
    
    return 0;
}