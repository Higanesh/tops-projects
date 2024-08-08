/*
Que21. Accept 2 numbers from user and swap 2 numbers with using 3rd variable and without using 3rd variable
*/

#include <stdio.h>
#include <stdbool.h>

void main() {
    
    int a,b;
    int temp=0;
    int choice;
    printf("Enter your choice(0/1)\n'0' for swap using 3rd variable\n'1' for swap without using 3rd variable\n");
    scanf("%d",&choice);
    if(choice == 1)
    {
        printf("Enter value of a & b\n");
        scanf("%d%d",&a,&b);
        printf("Before swapping\n");
        printf("Value of a = %d\n",a);
        printf("value of b = %d\n",b);
        temp = a;
        a = b;
        b = temp;
        printf("Swapping using 3rd variable\n");
        printf("Value of a = %d\n",a);
        printf("value of b = %d\n",b);
    }
    else if(choice == 0)
    {
        printf("Enter value of a & b\n");
        scanf("%d%d",&a,&b);
        printf("Before swapping\n");
        printf("Value of a = %d\n",a);
        printf("value of b = %d\n",b); 
        a = a + b;
        b = a - b;
        a = a - b;
        printf("Swapping without using 3rd variable\n");
        printf("Value of a = %d\n",a);
        printf("value of b = %d\n",b);
    }
    else
    {
        printf("You have enter wrong choice,please enter 0 or 1 only");
    }
    
}