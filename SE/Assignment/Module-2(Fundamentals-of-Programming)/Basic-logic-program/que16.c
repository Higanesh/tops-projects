/*
Que16. Convert country’s name in abbreviate form
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    
    char country[50];
    int len;
    printf("Enter country name\n");
    fgets(country, sizeof(country), stdin);
    country[strcspn(country, "\n")] = '\0';
    printf("%s\n",country);
    len = strlen(country);
    printf("Length is %d\n",len);
    printf("%c",toupper(country[0]));
    for(int i = 0; i <= len; i++){
        if(country[i] == ' ')
        {
            
            printf("%c",toupper(country[i+1]));
        }
    }
    return 0;
}
