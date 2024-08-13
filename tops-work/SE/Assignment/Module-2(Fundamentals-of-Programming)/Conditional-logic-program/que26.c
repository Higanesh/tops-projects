/*
Que26. Write a C program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit For next 100 units Rs. 0.75/unit For next 100 units Rs. 1.20/unit For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
*/

#include <stdio.h>
#include <string.h>

float calculate_bill(float unit,float charge_per_unit)
{
    printf("charge per unit is: %.2f\n",charge_per_unit);
    return unit * charge_per_unit;
}
int main()
{
    float electricity_bill,unit;
    printf("Enter unit consumed by the user\n");
    scanf("%f", &unit);
    if(unit <= 50){
        electricity_bill = calculate_bill(unit,0.50);
    }else if(unit >= 51 && unit <= 150){
        electricity_bill = calculate_bill(unit,0.75);
    }else if(unit >= 151 && unit < 250){
        electricity_bill = calculate_bill(unit,1.20);
    }else{
        electricity_bill = calculate_bill(unit,1.50);
    }
    printf("Unit consumed by user: %.2f\nElectricity bill: %.2f",unit,electricity_bill);
    return 0;
}
