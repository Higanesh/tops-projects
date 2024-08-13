/*
que6. Find the Character Is Vowel or Not
*/

#include <stdio.h>

int main()
{
    char c;
    printf("Enter any character\n");
    scanf("%c",&c);
    if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
    {
        printf("Character is VOWEL");
    }
    else
    {
        printf("Character is not VOWEL");
    }
    return 0;
}