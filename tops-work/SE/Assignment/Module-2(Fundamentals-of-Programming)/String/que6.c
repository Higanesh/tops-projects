/*
Que6. Write a program in C to count the total number of alphabets, digits and special characters in a string.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main()
{
    char str[20];
    int len;
    int alpha_counter = 0, digit_counter = 0, symbol_counter = 0;
    printf("Enter any string\n");
    fgets(str,sizeof(str),stdin);
    str[strcspn(str, "\n")] = '\0';
    len = strlen(str);
    for(int i = 0; i < len; i++)
    {
        if((str[i] >= 65 && str[i] <= 90) || (str[i] >= 97 && str[i] <= 122))
        {
            alpha_counter++;
        }else if(str[i] >= 48 && str[i] <= 57)
        {
            digit_counter++;
        }
        else
        {
            symbol_counter++;
        }
    }
    printf("Total number of alphabets: %d\n",alpha_counter);
    printf("Total number of digit: %d\n",digit_counter);
    printf("Total number of special character: %d",symbol_counter);
    return 0;
}