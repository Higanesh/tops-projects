/*
1] Write a C program to check whether a number is prime or not.
*/

#include <stdio.h>

int main() {
    
    int no,m;
    int flag = 0;
    printf("Enter any number\n");
    scanf("%d",&no);
    if(no == 1 || no == 2)
    {
        printf("Number is prime");
    }
    m = no;
    for(int i = 1; i < m/2; i++)
    {
        if(no % i != 0)
        {
            flag = 1;
        }
    }
    
    if(flag == 1)
    {
        printf("Number is PRIME");
    }
    else
    {
        printf("Number is not PRIME");
    }

    return 0;
}
