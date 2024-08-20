/*
17] Develop a C program that takes a string as input and removes all white spaces.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[50];
    printf("Enter any string\n");
    fgets(str,sizeof(str),stdin);
    int len = strlen(str);
    for(int i = 0; i < len; i++)
    {
        if(str[i] == ' ')
        {
            continue;
        }
        else
        {
            printf("%c",str[i]);
        }
    }
    return 0;
}
