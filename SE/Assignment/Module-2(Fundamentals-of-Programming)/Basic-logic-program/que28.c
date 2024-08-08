/*
Que28. Convert years into days and months
*/

#include <stdio.h>

void main() {

   float days,months,years;
   printf("Enter number of years\n");
   scanf("%f",&years);
   days = years * 365.25;
   months = years * 12;
   printf("%.2f years is approximately %.2f days\n",years,days);
   printf("%.2f years is approximately %.2f months",years,months);
   
}