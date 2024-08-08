/*
Que20. Accept monthly salary from the user and deduct 10% insurance premium, 10% loan installment find out of remaining salary.
*/

#include <stdio.h>

void main() {
    
    double salary,remSalary,insurancePremium,loanInstallment;
    printf("Enter salary amount\n");
    scanf("%lf",&salary);
    insurancePremium = salary * 0.10;
    loanInstallment = salary * 0.10;
    remSalary = salary - (insurancePremium+loanInstallment);
    printf("Remaining salary is %.2lf",remSalary);
    
}