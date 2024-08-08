/*
Que31. Convert kilometers into meters
*/

#include <stdio.h>

void main() {

   float meters,kilometers;
   printf("Enter number of kilometers\n");
   scanf("%f",&kilometers);
   meters = kilometers * 1000;
   printf("%.2f kilometers is equal to %.2f meters\n",kilometers,meters);
   
}