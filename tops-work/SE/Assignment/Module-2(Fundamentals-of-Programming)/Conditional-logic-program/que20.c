/*
Que20. If bill exceeds Rs. 800 then a surcharge of 18% will be charged and the minimum bill should be of Rs. 256/-
*/

#include <stdio.h>
const float surcharge = 1.18;
float cal_final_bill(float bill)
{
    if(bill < 256){
        bill = 256;
        return bill;
    }else if(bill > 800){
        bill *= surcharge;
    }else{
        return bill;
    }
}
int main() {
    
    float bill;
    printf("Enter your bill amount\n");
    scanf("%f",&bill);
    printf("Your final bill amount is %.2f",cal_final_bill(bill));
    return 0;
}