/*
Que13. WAP to accept 5 numbers from user and check entered number is even or odd using of array
*/

#include <stdio.h>

int main()
{
    int array[5];
    printf("Enter 5 integer numbers\n");
    for(int i = 0; i < 5; i++){
        scanf("%d",&array[i]);
        if(array[i] % 2 == 0){
            printf("%d is even\n",array[i]);
        }
        else{
            printf("%d is odd\n",array[i]);
        }
    }
    return 0;
}