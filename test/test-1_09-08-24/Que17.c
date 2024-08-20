/*
17] Create a function in C that checks if a given string is a
palindrome.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>


bool palindrom(char str[20])
{
    int len = strlen(str);
    char reverse_str[20];
    printf("The reverse string is\n");
    for(int i = 0; i < len; i++)
        {
             reverse_str[i] = str[len - 1 - i];
        }
    reverse_str[len] = '\0';
    printf("%s\n",reverse_str);
    for(int i = 0; i < len; i++)
    {
        if(reverse_str[i] != str[i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    char str[20];
    printf("Enter any string for reverse operation\n");
    scanf("%s",&str);
    printf("The original string is\n%s\n",str);
    
    if(palindrom(str))
    {
        printf("String is PALINDROM");
    }
    else
    {
        printf("String is not PALINDROM");
    }
    return 0;
}

