/*
*           
* *         
* * *       
* * * *     
* * * * *   
* * * * * * 
* * * * *   
* * * *     
* * *       
* *         
*       
*/

#include <stdio.h>

int main() {
    int num = 6;
    for(int row = 1; row <= num; row++){
        for(int col = 1; col <= row; col++){
            printf("* ");
        }
        for(int col = 1; col <= num-row; col++){
            printf("  ");
        }
        printf("\n");
    }
    for(int row = 1; row <= num; row++){
        for(int col = 1; col <= num-row; col++){
            printf("* ", row);
        }
        for(int col = 1; col <= row; col++){
            printf("  ");
        }
        printf("\n");
    }
    return 0;
}
