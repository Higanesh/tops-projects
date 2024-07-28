/*
Que10. find the area of a rectangular prism formula : A=2(wl+hl+hw)
*/

#include <stdio.h>

void main() {
    
    float length,width,height;
    double areaOfPrism;
    printf("Enter a value of length, width, and height\n");
    scanf("%f %f %f",&length,&width,&height);
    areaOfPrism = 2*((length*width) + (width*height) + (height*length));
    printf("Area of rectangular prism is %.2f square unit",areaOfPrism);

}
