/*
Que23. WAP to calculate swap 2 numbers with using of multiplication and division.
*/

#include <stdio.h>

void main() {
    
        int a,b;
        printf("Enter value of a & b\n");
        scanf("%d%d",&a,&b);
        printf("Before swapping\n");
        printf("Value of a = %d\n",a);
        printf("value of b = %d\n",b);
        a = a * b;
        b = a / b;
        a = a / b;
        printf("Swapping using multiplication and division\n");
        printf("Value of a = %d\n",a);
        printf("value of b = %d\n",b);
    
}