/*
Que15. Convert school’s name in abbreviated form
Suman High School No. 6
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    
    char school[50];
    int len;
    printf("Enter school name\n");
    fgets(school, sizeof(school), stdin);
    school[strcspn(school, "\n")] = '\0';
    printf("%s\n",school);
    len = strlen(school);
    printf("Length is %d\n",len);
    printf("%c",toupper(school[0]));
    for(int i = 0; i <= len; i++){
        if(school[i] == ' ')
        {
            printf("%c",toupper(school[i+1]));
        }
    }
    return 0;
}