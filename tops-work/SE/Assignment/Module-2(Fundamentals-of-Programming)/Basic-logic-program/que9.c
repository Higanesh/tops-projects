/*
Que9. Find circumference of Triangle formula : triangle = a + b + c
*/

#include <stdio.h>

void main() {
    
    float a,b,c;
    double circumferenceOfTriangle;
    printf("Enter a value of a, b, and c\n");
    scanf("%f %f %f",&a,&b,&c);
    circumferenceOfTriangle = a + b + c;
    printf("Circumference of triangle is %.2f square unit",circumferenceOfTriangle);

}