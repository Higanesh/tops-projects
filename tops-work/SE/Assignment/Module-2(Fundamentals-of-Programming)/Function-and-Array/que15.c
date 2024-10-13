/*
Que15. Store 5 numbers in array and sort it in ascending order
*/

#include <stdio.h>

int main() {
    
    int array[5];
    int temp;
    printf("Enter array elements\n");
    for(int i = 0; i < 5; i++)
    {
         scanf("%d",&array[i]);
    }
        for(int i = 0; i < 5 -1; i++){
            for(int j = 0; j < 5 - 1; j++)
            {
                 if(array[j] > array[j+1])
                {
                    temp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    printf("sorted array\n");
    for(int k = 0; k < 5; k++)
    {
        printf("%d\n",array[k]);
    }
    return 0;
}