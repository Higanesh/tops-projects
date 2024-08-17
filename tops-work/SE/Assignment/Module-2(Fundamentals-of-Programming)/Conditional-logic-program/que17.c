/*
Que17. Write a C program to check whether a triangle can be formed with the given values for the angles.
*/

#include <stdio.h>

int main()
{
    float angle1,angle2,angle3,sum;
    printf("Enter values of angle1,angle2 & angle3\n");
    scanf("%f%f%f",&angle1,&angle2,&angle3);
    printf("angle1 = %.2f\nangle2 = %.2f\nangle3 = %.2f\n",angle1,angle2,angle3);
    sum = angle1 + angle2 + angle3;
    if(sum == 180 && angle1 > 0 && angle2 > 0 && angle3 > 0)
    {
        printf("The angles form a valid triangle.\n");
    }
    else
    {
        printf("The angles do not form a valid triangle.\n");
    }
    return 0;
}