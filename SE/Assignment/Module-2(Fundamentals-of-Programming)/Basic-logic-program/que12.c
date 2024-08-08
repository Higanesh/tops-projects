/*
Que12. Accept number of students from user. I need to give 5 apples to each student. How many apples are required?
*/

#include <stdio.h>

void main() {
    
    int numberOfStudents,numberOfAppleToEachStudents = 5,requiredApple;
    printf("Enter number of students\n");
    scanf("%d",&numberOfStudents);
    requiredApple = numberOfStudents * numberOfAppleToEachStudents;
    printf("Total number of apple required is %d",requiredApple);
    
}