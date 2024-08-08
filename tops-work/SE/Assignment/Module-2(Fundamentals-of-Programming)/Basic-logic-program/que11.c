/*
Que11. Find circumference of square formula : C = 4 * a
*/

#include <stdio.h>

void main() {
    
    float length;
    double circumferenceOfSquare;
    printf("Enter a value of length\n");
    scanf("%f",&length);
    circumferenceOfSquare = 4 * length;
    printf("Circumference of square is %.2f square unit",circumferenceOfSquare);
    
}