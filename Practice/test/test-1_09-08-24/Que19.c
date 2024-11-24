/*
19] Develop a C program that reverses the digits of an integer number
entered by the user.
*/

#include <stdio.h>

int main() {
    
    int num,reverse_num = 0;
    printf("Enter any number\n");
    scanf("%d",&num);
    for(;num != 0; num /= 10)
    {
        int digit = num % 10;
        reverse_num = reverse_num * 10 + digit;
    }
    printf("Reverse number is: %d",reverse_num);

    return 0;
}
