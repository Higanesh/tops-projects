/*
Que13. Write a program in C to remove characters from a string except alphabets.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[50];
    printf("Enter any string\n");
    scanf("%s",str);
    int len = strlen(str);
    for(int i = 0; i < len; i++)
    {
        if((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z'))
        {
            printf("%c",str[i]);
        }
        else
        {
            continue;
        }
    }
    
    return 0;
}