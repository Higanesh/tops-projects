/*
Que8. Write a program in C to count the total number of vowels or consonants in a string.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[50];
    int vow_counter = 0,conso_counter = 0;
    printf("Enter any string\n");
    scanf("%s",str);
    int len = strlen(str);
    for(int i = 0; i < len; i++)
    {
        if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' || str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U')
        {
            vow_counter++;
        }
        else if((str[i] >= 97 && str[i] <= 122) || (str[i] >= 65 && str[i] <= 90))
        {
            conso_counter++;
        }
        else
        {
            continue;
        }
    }
    printf("Total number vowels in string:     %d\n",vow_counter);
    printf("Total number consonants in string: %d\n",conso_counter);
    return 0;
}