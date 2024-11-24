/*
20] Implement a C program that converts temperature from Celsius to Fahrenheit using the
formula F = (C × 9/5) + 32.
*/

#include <stdio.h>

void main() {
    
   float fahrenheit,celsius;
   printf("Enter Fahrenheit to convert into Celsius\n");
   scanf("%f",&fahrenheit);
   celsius = (fahrenheit - 32) * 5/9;
   printf("Temperature is %.2f fahrenheit\n",fahrenheit);
   printf("Temperature is %.2f celsius",celsius);

}