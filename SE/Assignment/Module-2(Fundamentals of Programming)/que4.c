/*
Que4. Find Area of Square formula : a = a2
*/

#include <stdio.h>

void main() {
    
    float sideLength;
    double areaOfSquare;
    printf("Enter a value of side length\n");
    scanf("%f",&sideLength);
    areaOfSquare = sideLength * sideLength;
    printf("Area of square is %.2f square unit",areaOfSquare);

}