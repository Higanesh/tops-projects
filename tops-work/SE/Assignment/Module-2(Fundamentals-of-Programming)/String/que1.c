/*
Que1. Write a program in C to find the length of a string without using library functions.
*/

#include <stdio.h>
#include <string.h>

int length(char str[20])
{
    int i = 0;
    while(str[i] != '\0')
    {
        i++;
    }
    return i;
}

int main()
{
    char str[20];
    printf("Enter string\n");
    scanf("%s",str);
    printf("The length of string is: %d",length(str));
    return 0;
}