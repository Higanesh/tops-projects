/*
17] Create a function in C that checks if a given string is a
palindrome.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char str[20];
    char reverse_str[20];
    bool flag = false;
    printf("Enter any string for reverse operation\n");
    scanf("%s",&str);
    printf("The original string is\n%s\n",str);
    int len = strlen(str);
    printf("The reverse string is\n");
    for(int i = 0; i < len; i++)
        {
             reverse_str[i] = str[len - 1 - i];
        }
    printf("%s\n",reverse_str);
    for(int i = 0; i < len; i++)
    {
        if(reverse_str[i] == str[i])
        {
            flag = true;
        }
        else{
            flag = false;
        }
        
    }
    if(flag)
    {
        printf("String is PALINDROM");
    }
    else
    {
        printf("String is not PALINDROM");
    }
    return 0;
}

