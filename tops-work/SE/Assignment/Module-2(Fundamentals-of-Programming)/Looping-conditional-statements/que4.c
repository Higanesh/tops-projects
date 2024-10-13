/*
Que4. WAP to print table up to given numbers
*/

#include <stdio.h>

int main()
{
    int no,counter = 1;
    printf("Enter any number\n");
    scanf("%d",&no);
    while(counter <= no)
    {
        printf("Table of %d\n",counter);
        for(int i = 1; i <= 10; i++)
        {
            printf("%d * %d = %d\n",counter,i,counter*i);
        }
        printf("\n");
        counter++;
    }
    return 0;
}