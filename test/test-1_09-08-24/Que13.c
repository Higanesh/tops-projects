/*
13] Write a program in C that reverses a given string without using
any built-in functions.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[20];
    char temp;
    char reverse_str[20];
    printf("Enter any string for reverse operation\n");
    scanf("%s",&str);
    printf("The original string is\n%s\n",str);
    int len = strlen(str);
    printf("The reverse string is\n");
    for(int i = len-1; i >= 0; i--)
    {
        printf("%c",str[i]);
    }
    return 0;
}