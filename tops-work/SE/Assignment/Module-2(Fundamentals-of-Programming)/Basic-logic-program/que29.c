/*
Que29. Convert minutes into seconds and hours
*/

#include <stdio.h>

void main() {

   float seconds,minutes,hours;
   printf("Enter number of minutes\n");
   scanf("%f",&minutes);
   seconds = minutes * 60;
   hours = minutes / 60;
   printf("%.2f minutes is equal to %.2f seconds\n",minutes,seconds);
   printf("%.2f minutes is equal to %.2f hours",minutes,hours);

}