/*
Que10. Write a program in C to extract a substring from a given string.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[50];
    int start,end;
    printf("Enter any string\n");
    scanf("%s",str);
    printf("Enter start and end index of substring\n");
    scanf("%d%d",&start,&end);
    int len = strlen(str);
    for(int i = start; i <= end; i++)
    {
        if(start < 0 || start > end || start > len || end > len)
        {
            printf("Invalid Input");
        }
        else
        {
            printf("%c",str[i]);    
        }
    }
    return 0;
}