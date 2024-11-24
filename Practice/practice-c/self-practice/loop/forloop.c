#include <stdio.h>

void main()
{
    int n = 4;
    for(int r = 0; r <= n; r++){
        for(int c = 0; c <= n-r; c++){
            printf("  ");
        }
        for(int c = 0; c <= r; c++){
            printf("* ");
        }
        printf("\n");
    }
    for(int r = 4; r >= 0; r--){
       for(int c = 0; c <= n-r+1; c++){
           printf("  ");
       } 
       for(int c = 0; c <= r-1; c++){
           printf("* ");
       }
       printf("\n");
    }
}



