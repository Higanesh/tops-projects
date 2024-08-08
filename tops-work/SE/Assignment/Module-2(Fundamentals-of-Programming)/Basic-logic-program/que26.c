/*
Que26. Convert temperature Fahrenheit to Celsius
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