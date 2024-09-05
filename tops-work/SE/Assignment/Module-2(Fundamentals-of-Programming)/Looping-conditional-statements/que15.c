/*
Que15. Calculate sum of 10 numbers using of while loop
*/

#include <stdio.h>

int main(){
    int count = 1,num,sum = 0;
    while(count <= 10){
    scanf("%d",&num);
    sum = sum + num;
    count++;
}
printf("%d",sum);
}