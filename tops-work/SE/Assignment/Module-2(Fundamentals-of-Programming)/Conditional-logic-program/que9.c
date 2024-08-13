/*
Que9. C Program to Check Uppercase or Lowercase or Digit or Special Character
*/

#include <stdio.h>

int main()
{
    char c;
    printf("Enter any character\n");
    scanf("%c",&c);
    if(c >= 'A' && c <= 'Z')
    {
        printf("Character is Uppercase");
    }
    else if(c >= 'a' && c <= 'z')
    {
        printf("Character is Lowercase");
    }
    else if(c >= '0' && c <= '9')
    {
        printf("Character is Digit");
    }
    else
    {
        printf("Character is Special Character");
    }
    return 0;
}