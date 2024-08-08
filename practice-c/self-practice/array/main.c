/*
char name[] = "PyThoN cOde"
- lower_case - "python code"
- upper_case - "PYTHON CODE"
- swap_case - "pYtHOn CoDE"
- title_case - "Python Code"
- capitlize_case - "Python code"
- length_count - 11
*/

#include <stdio.h>
#include <string.h>

void lowerCase(char name[],int len)
{
    for(int pos = 0; pos < len; pos++)
    {
        if(name[pos] >= 97 && name[pos] <= 122)
        {
            printf("%c",name[pos]);
        }
        else
        {
            name[pos] += 32;
            printf("%c",name[pos]);
        }
    }
    printf("\n");
}

void upperCase(char name[],int len)
{
    for(int pos = 0; pos < len; pos++)
    {
        if(name[pos] >= 65 && name[pos] <= 90)
        {
            printf("%c",name[pos]);
        }
        else
        {
            name[pos] -= 32;
            printf("%c",name[pos]);
        }
    }
    printf("\n");
}

void swapCase(char name[],int len)
{
    for(int pos = 0; pos < len; pos++)
    {
        if(name[pos] >= 65 && name[pos] <= 90)
        {
            name[pos] += 32;
            printf("%c",name[pos]);
        }
        else
        {
            name[pos] -= 32;
            printf("%c",name[pos]);
        }
    }
    printf("\n");
}
//GANesh
void titleCase(char name[],int len)
{
    for(int pos = 0; pos < len; pos++)
    {
        if(pos == 0)
        {
            if(name[pos] >= 97 && name[pos] <= 122)
            {
                name[pos] -= 32;
            }
        }
        else
        {
            if(name[pos] >= 65 && name[pos] <= 90)
            {
                name[pos] += 32;
            }
        }
        printf("%c",name[pos]);
    }
    printf("\n");
}

//capitalize case
void capitalizeCase(char name[],int len)
{
    for(int pos = 0; pos < len; pos++)
    {
        if(pos == 0)
        {
            if(name[pos] >= 97 && name[pos] <= 122)
            {
                name[pos] -= 32;
            }
        }
        else
        {
            if(name[pos] >= 65 && name[pos] <= 90)
            {
                name[pos] += 32;
            }
        }
        printf("%c",name[pos]);
    }
    printf("\n");
}

int main() {
    
    char name[20];
    printf("enter any string\n");
    //scanf("%s",name);
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = '\0';
    int len = strlen(name); 
    //(sizeof(name)/sizeof(name[0]))-1;
    printf("Length of string is %d\n",len);
    lowerCase(name,len);
    upperCase(name,len);
    swapCase(name,len);
    titleCase(name,len);
    capitalizeCase(name,len);

}
