/*
Que11. Accept 5 names from user at run time.
*/

#include <stdio.h>
#include <string.h>
int main()
{
    char name[5][50];
    printf("Take 5 names from user\n");
    int i = 0;
    while(i < 5)
    {
        fgets(name[i], sizeof(name), stdin);
        i++;
    }
    
    int j = 0;
    while(j < 5)
    {
        printf("%s",name[j]);
        j++;
    }
    return 0;
}