/*
Que7. Find area of Rectangle Formula : A=wl
*/

#include <stdio.h>

void main() {
    
    float width,length;
    double areaOfRectangle;
    printf("Enter a value of width & length\n");
    scanf("%f %f",&width,&length);
    areaOfRectangle = width * length;
    printf("Area of rectangle is %.2f square unit",areaOfRectangle);

}