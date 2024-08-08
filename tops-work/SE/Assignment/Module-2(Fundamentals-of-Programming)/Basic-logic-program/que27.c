/*
Que27. Convert days into months
*/

#include <stdio.h>

void main() {

   float days,months;
   const float avgNoOfDaysInMonth = 30.44;
   printf("Enter number of days in a month\n");
   scanf("%f",&days);
   months = days / avgNoOfDaysInMonth;
   printf("%.2f days is approximately %.2f months",days,months);
   
}