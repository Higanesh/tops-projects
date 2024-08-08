/*
Que5. Find Area of Cube formula : a = 6a2
*/

#include <stdio.h>

void main() {
    
    float sideLength;
    double areaOfCube;
    printf("Enter a value of side length\n");
    scanf("%f",&sideLength);
    areaOfCube = 6 * sideLength * sideLength;
    printf("Area of cube is %.2f square unit",areaOfCube);

}