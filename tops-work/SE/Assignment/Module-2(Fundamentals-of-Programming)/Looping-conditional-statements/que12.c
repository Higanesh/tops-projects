/*
Que12. Program of Armstrong Number in C Using For Loop & While Loop
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int digit[20];
    int real_num,num,counter = 0,temp=0,sum=0;
    printf("Enter any number\n");
    scanf("%d",&num);
    real_num = abs(num);
    while(real_num > 0)
    {
        digit[counter] = real_num % 10;
        real_num = real_num / 10;
        counter++;
    }
    for(int i = 0; i < counter; i++)
    {
        sum += pow(digit[i],counter);
    }
    if(real_num == sum)
    {
        printf("Number is Armstrong\n");
    }else{
        printf("Number is not Armstrong");
    }
    return 0;
}