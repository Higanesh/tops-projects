/*
Que24. Accept 5 employees name and salary and count average and total salary
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char name[5][50];
    double sal[5],totalSal,averageSal;
    printf("Enter five employees name & salary\n");
    for(int i = 0; i < 5; i++)
    {
        scanf("%s%lf",name[i],&sal[i]);
    }
    
    for(int i = 0; i < 5; i++)
    {
        printf("%s\t%.2lf\n",name[i],sal[i]);
        totalSal += sal[i];
    }
    averageSal = totalSal/5;
    printf("Average salary of enployee is %.2lf",averageSal);
    
    return 0;
}