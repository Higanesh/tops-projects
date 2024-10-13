/*
Que4. Write a program in C to count the total number of words in a string.
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char str[100];
    int counter = 1;
    printf("Enter any string\n");
    fgets(str, sizeof(str), stdin);
    printf("%s\n",str);
    int i = 0;
    while(str[i] != '\n')
    {
        if(str[i] == ' ')
        {
            counter++;
        }
        i++;
    }
    printf("Total number of words in a string is: %d",counter);
    return 0;
}