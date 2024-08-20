/*
Que11. Write a program in C to read a sentence and replace lowercase characters with uppercase and vice versa.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[50];
    printf("Enter any string\n");
    fgets(str,sizeof(str),stdin);
    str[strcspn(str, "\n")] = '\0';
    int len = strlen(str);
    //printf("%d\n",len);
    for(int i = 0; i < len; i++)
    {
        if(str[i] >= 65 && str[i] <= 90)
        {
            printf("%c",str[i]+32);
        }
        else if(str[i] >= 97 && str[i] <= 122)
        {
            printf("%c",str[i]-32);
        }
        else
        {
            printf("%c",str[i]);
        }
    }
    return 0;
}