/*
19] Explain what a pointer to a pointer is in C and give an example.

Ans: pointer is variable which is use to store memory location of the another variable.
syntax int *ptr;
for eg. int *ptr;
        int no = 10;
        ptr = &no;
*/

#include <stdio.h>

int main()
{
    int *ptr;
    int no = 20;
    ptr = &no;

    printf("%d",*ptr);
    return 0;
}