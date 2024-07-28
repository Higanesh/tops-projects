/*
Que3. WAP to Find Area And Circumference of Circle
*/

#include <stdio.h>

void main() {
    
    const double PI = 3.14;
    float r;
    double areaOfCircle,circumferenceOfCircle;
    printf("Enter value of radius 'r'\n");
    scanf("%f",&r);
    areaOfCircle = PI * r * r;
    circumferenceOfCircle = 2 * PI * r;
    printf("Area of circle : %.2f square unit\n",areaOfCircle);
    printf("Circumference of circle : %.2f unit",circumferenceOfCircle);

}