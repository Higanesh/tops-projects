/*
Que8. WAP to accept the height of a person in centimeters and categorize the person according to their height.
*/

#include <stdio.h>

int main()
{
    float height;
    printf("Enter the height of the person in centimeters:\n");
    scanf("%f", &height);

    if (height < 150.0) {
        printf("The person is categorized as Short.\n");
    }
    else if (height >= 150.0 && height <= 180.0) {
        printf("The person is categorized as Average height.\n");
    }
    else {
        printf("The person is categorized as Tall.\n");
    }
    return 0;
}