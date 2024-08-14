/*
10] Write a function in C that takes an integer and returns its square.
*/

#include <stdio.h>

int square(int no)
{
    return no * no;
}

int main() {
    
    int no;
    printf("Enter any number\n");
    scanf("%d",&no);
    printf("Square of %d number is %d",no,square(no));

    return 0;
}