/*
Que5. Write a program in C to compare two strings without using string library functions.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char str1[20];
    char str2[20];
    int len1,len2;
    bool flag = false;
    printf("Enter first string\n");
    scanf("%s",str1);
    printf("Enter second string\n");
    scanf("%s",str2);
    len1 = strlen(str1);
    len2 = strlen(str2);
    if(len1 == len2)
    {
        for(int i = 0; i < len1; i++)
        {
            if(str1[i] == str2[i])
            {
                flag = true;
            }
            else
            {
                flag = false;
            }
        }
    }
    
    if(flag)
    {
        printf("String is equal");
    }else{
        printf("String is not equal");
    }
    return 0;
}