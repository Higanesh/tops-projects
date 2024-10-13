/*
Que7. Write a program in C to copy one string to another string.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str1[50];
    char str2[50];
    printf("Enter first string\n");
    scanf("%s",str1);
    int len1 = strlen(str1);
    for(int i = 0; i < len1; i++)
    {
        str2[i] = str1[i];
    }
    str2[len1] = '\0';
    printf("Original string: %s\n",str1);
    printf("Copied string:   %s",str2);
    return 0;
}