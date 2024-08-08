/*
Que25. Accept 5 expense from user and find average of expense
*/

#include <stdio.h>
#include <string.h>

int main()
{
    char expense[5][50];
    double amt[5],totalAmt;
    double averageAmt = 0;
    printf("Enter five expense\n");
    for(int i = 0; i < 5; i++)
    {
        scanf("%s%lf",expense[i],&amt[i]);
    }
    
    for(int i = 0; i < 5; i++)
    {
        printf("%s\t%.2lf\n",expense[i],amt[i]);
        totalAmt += amt[i];
    }
    averageAmt = totalAmt/5;
    printf("Average of expense is %.2lf",averageAmt);
    
    return 0;
}