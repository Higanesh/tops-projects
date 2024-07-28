/*
Que8. Find circumference of Rectangle formula : C = 4 * a
*/

#include <stdio.h>

void main() {
    
    float width,length;
    double circumferenceOfRectangle;
    printf("Enter a value of width & length\n");
    scanf("%f %f",&width,&length);
    circumferenceOfRectangle = 2 * (width + length);
    printf("Circumference of rectangle is %.2f square unit",circumferenceOfRectangle);
    
}
