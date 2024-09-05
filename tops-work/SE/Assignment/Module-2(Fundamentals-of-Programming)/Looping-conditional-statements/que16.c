/*
Que16. Calculate the Sum of Natural Numbers Using the While Loop
*/

#include <stdio.h>

int main(){
    int count = 1,num,sum = 0,size;
    printf("Enter count of numbers for sum\n");
    scanf("%d",&size);
    printf("Enter %d numbers for sum\n",size);
    while(count <= size){
    scanf("%d",&num);
    sum = sum + num;
    count++;
}
printf("%d",sum);
}