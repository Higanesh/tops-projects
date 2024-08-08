/*
Que30. WAP to convert years into days and days into years
*/

#include <stdio.h>

void main() {

   float years,days;
   printf("Enter number of years\n");
   scanf("%f",&years);
   days = years * 365.25;
   printf("%.2f years is approximately %.2f days\n",years,days);
   printf("Enter number of days\n");
   scanf("%f",&days);
   years = days / 365.25;
   printf("%.2f days is approximately %.2f years",days,years);

}