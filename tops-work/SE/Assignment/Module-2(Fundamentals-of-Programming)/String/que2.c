/*
Que2. Write a program in C to separate individual characters from a string.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[20];
    char temp;
    char reverse_str[20];
    printf("Enter any string\n");
    scanf("%s",&str);
    printf("The original string is\n%s\n",str);
    int len = strlen(str);
    for(int i = 0; i < len; i++)
    {
        printf("Character at index %d is: %c\n",i,str[i]);
    }
    return 0;
}