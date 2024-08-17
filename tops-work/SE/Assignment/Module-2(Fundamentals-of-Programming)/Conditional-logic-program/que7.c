/*
Que7. Accept marks from user and check pass or fail
*/

#include <stdio.h>

int main()
{
    int marks1,marks2,marks3;
    printf("Enter marks of three subjects\n");
    scanf("%d%d%d",&marks1,&marks2,&marks3);
    printf("marks1 = %d\nmarks2 = %d\nmarks3 = %d\n",marks1,marks2,marks3);
    if(marks1 >= 35 && marks2 >= 35 && marks3 >= 35)
    {
        printf("PASS");
    }
    else
    {
        printf("FAIL");
    }
    return 0;
}