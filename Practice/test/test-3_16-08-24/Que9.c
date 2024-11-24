/*
9] Implement a C program that multiplies two matrices.
*/

#include <stdio.h>

int main() {
    
    int matrix1[3][3] = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    int matrix2[3][3] = {
        {11,22,33},
        {44,55,66},
        {77,88,99}
    };
    
    int len_of_row = sizeof(matrix1)/sizeof(matrix1[0]);
    int len_of_col = (sizeof(matrix1[0])/sizeof(matrix1[0][0]));
    
    printf("Matrix-1:\n");
    for(int row = 0; row<len_of_row; row++){
        for(int col = 0; col<len_of_col; col++){
            printf("%d ", matrix1[row][col]);
        }
        printf("\n");
    }
    
    printf("Matrix-2:\n");
    for(int row = 0; row<len_of_row; row++){
        for(int col = 0; col<len_of_col; col++){
            printf("%d ", matrix2[row][col]);
        }
        printf("\n");
    }
    printf("Matrix-1 * Matrix-2:\n");
    for(int row = 0; row<len_of_row; row++){
        for(int col = 0; col<len_of_col; col++){
            printf("%d ",matrix1[row][col] * matrix2[row][col]);
        }
        printf("\n");
    }
    return 0;
}