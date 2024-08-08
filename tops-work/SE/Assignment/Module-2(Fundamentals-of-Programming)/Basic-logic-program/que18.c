/*
Que18. Calculate person’s Annual salary
*/

#include <stdio.h>

void main() {
    
    double monthlySal,annualSal;
    printf("Enter persons monthly salary\n");
    scanf("%lf",&monthlySal);
    annualSal = 12 * monthlySal;
    printf("Persons annual salary is %.2lf",annualSal);

}