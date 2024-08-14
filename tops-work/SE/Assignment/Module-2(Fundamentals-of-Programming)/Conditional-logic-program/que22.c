/*
Que22. Write a C program to input basic salary of an employee and calculateits Gross salary according to following:
Basic Salary <= 10000 : HRA = 20%, DA = 80% Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%\
*/

#include <stdio.h>

float cal_gross_sal(float basic_sal,float hra,float da){
    float gross_sal =  basic_sal+hra+da;
    return gross_sal;
}
int main() {
    
    float basic_sal;
    float hra, da;
    printf("Enter basic salary amount\n");
    scanf("%f",&basic_sal);
    if(basic_sal <= 10000){
        hra = 10000 * 0.20;
        da = 10000 * 0.80;
        printf("Gross salary is %.2f",cal_gross_sal(basic_sal,hra,da));
    }else if(basic_sal <= 20000){
        hra = 10000 * 0.25;
        da = 10000 * 0.90;
        printf("Gross salary is %.2f",cal_gross_sal(basic_sal,hra,da));
    }else{
        hra = 10000 * 0.30;
        da = 10000 * 0.95;
        printf("Gross salary is %.2f",cal_gross_sal(basic_sal,hra,da));
    }
    
    return 0;
}