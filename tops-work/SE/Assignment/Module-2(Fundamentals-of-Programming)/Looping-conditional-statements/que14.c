/*
Que14. Accept 5 numbers from user and find those numbers factorials
*/

#include <stdio.h>

int main()
{
    int no[5],fact = 1;
    printf("Enter 5 numbers for calculate the factorial each number\n");
    for(int i = 0; i < 5; i++)
    {
        scanf("%d",&no[i]);
    }
    for(int i = 0; i < 5; i++){
        printf("Factorial of %d is: ",no[i]);
         while(no[i] > 0)
        {
            fact = fact * no[i];
            no[i]--;
        }
        printf("%d\n",fact);
        fact = 1;
    }
    return 0;
}
