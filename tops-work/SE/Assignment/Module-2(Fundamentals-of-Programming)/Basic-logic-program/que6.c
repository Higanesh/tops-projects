/*
Que6. Find area of Triangle Formula : A = 1/2 × b × h
*/

#include <stdio.h>

void main() {
    
    float width,height;
    double areaOfTriangle;
    printf("Enter a value of width & height\n");
    scanf("%f %f",&width,&height);
    areaOfTriangle = 0.5 * width * height;
    printf("Area of triangle is %.2f square unit",areaOfTriangle);

}