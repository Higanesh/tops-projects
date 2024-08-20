/*
2] Implement a C program that reads a string from the user and counts the number of vowels and
consonants in it.
*/

#include <stdio.h>
#include <string.h>
int main() {
    
    char str[20];
    int vow_counter = 0,cons_counter = 0;
    int len;
    printf("Enter any string\n");
    scanf("%s",&str);
    len = strlen(str);
    for(int i = 0; i < len; i++)
    {
        if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u' || str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' || str[i] == 'U')
        {
            vow_counter++;
        }
        else if((str[i] >= 65 && str[i] <= 90) || (str[i] >= 97 && str[i] <= 122))
        {
            cons_counter++;
        }
        else
        {
            continue;
        }
    }
    printf("Number of vowels %d\n",vow_counter);
    printf("Number of consonants %d\n",cons_counter);
    return 0;
}
