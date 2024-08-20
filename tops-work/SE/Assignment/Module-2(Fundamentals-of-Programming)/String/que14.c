/*
Que14. Write a program in C to combine two strings manually
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str1[50];
    char str2[50];
    printf("Enter first string\n");
    scanf("%s",str1);
    printf("Enter second string\n");
    scanf("%s",str2);
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    for(int i = 0; i < len2; i++)
    {
        str1[i+len1] = str2[i];
    }
    printf("%s",str1);
    return 0;
}