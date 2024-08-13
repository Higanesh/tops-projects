/*
Que19. Write a program in C to calculate and print the electricity bill of a given customer. The customer ID, name, and unit consumed by the user should be captured from the keyboard to display the total amount to be paid to the customer. The charge are as follow :
    Unit                              Charge/unit
upto 350                                @1.20
350 and above but less than 600         @1.50
600 and above but less than 800         @1.80
800 and above                           @2.00
*/

#include <stdio.h>
#include <string.h>

float calculate_bill(float unit,float charge_per_unit)
{
    return unit * charge_per_unit;
}
int main()
{
    float electricity_bill,unit;
    char name[20];
    int cust_id;
    printf("Enter Customer Id,name and unit consumed by the user\n");
    scanf("%d", &cust_id);
    getchar(); // to consume the newline left by scanf
    fgets(name, sizeof(name), stdin);
    int len = strlen(name);
    if (len > 0 && name[len - 1] == '\n') {
        name[len - 1] = '\0';
    }
    scanf("%f", &unit);
    if(unit < 350){
        electricity_bill = calculate_bill(unit,1.20);
    }else if(unit >= 350 && unit < 600){
        electricity_bill = calculate_bill(unit,1.50);
    }else if(unit >= 600 && unit < 800){
        electricity_bill = calculate_bill(unit,1.80);
    }else{
        electricity_bill = calculate_bill(unit,2.00);
    }
    printf("Customer ID: %d\nCustomer name: %s\nUnit consumed by user: %.2f\nElectricity bill: %.2f",cust_id,name,unit,electricity_bill);
    return 0;
}