/*
Que17. Calculate person’s insurance premium based on salary
*/

#include <stdio.h>

void main() {
    
    double salary,premium;
    double premiumRate = 0.05;
    printf("Enter persons annual salary\n");
    scanf("%lf",&salary);
    premium = salary * premiumRate;
    printf("Persons annual premium is %.2lf",premium);
    
}