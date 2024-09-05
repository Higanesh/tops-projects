/*
Que6. WAP to make addition, Subtraction and multiplication of two matrix using 2-D Array
*/


#include <stdio.h>

void addMatrix(int matrix1[3][4],int matrix2[3][4],int len_of_row,int len_of_col){
    printf("Matrix-1 + Matrix-2:\n");
    for(int row = 0; row<len_of_row; row++){
        for(int col = 0; col<len_of_col; col++){
            printf("%d ",matrix1[row][col] + matrix2[row][col]);
        }
        printf("\n");
    }
}

void subtractMatrix(int matrix1[3][4],int matrix2[3][4],int len_of_row,int len_of_col){
    printf("Matrix-1 - Matrix-2:\n");
    for(int row = 0; row<len_of_row; row++){
        for(int col = 0; col<len_of_col; col++){
            printf("%d ",matrix1[row][col] - matrix2[row][col]);
        }
        printf("\n");
    }
}

void multiMatrix(int matrix1[3][4],int matrix2[3][4],int len_of_row,int len_of_col){
    printf("Matrix-1 * Matrix-2:\n");
    for(int row = 0; row<len_of_row; row++){
        for(int col = 0; col<len_of_col; col++){
            printf("%d ",matrix1[row][col] * matrix2[row][col]);
        }
        printf("\n");
    }
}

int main() {
    
    int matrix1[3][4] = {
        {1,2,3,0},
        {4,5,6,0},
        {7,8,9,0}
    };
    int matrix2[3][4] = {
        {11,22,33,0},
        {44,55,66,0},
        {77,88,99,0}
    };
    
    // printf("%d", matrix[1][1]);
    
    int len_of_row = sizeof(matrix1)/sizeof(matrix1[0]);
    int len_of_col = (sizeof(matrix1[0])/sizeof(matrix1[0][0]));
    
    // printf("Row : %d, Col : %d", len_of_row,len_of_col);
    
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
    
    addMatrix(matrix1,matrix2,len_of_row,len_of_col);
    subtractMatrix(matrix1,matrix2,len_of_row,len_of_col);
    multiMatrix(matrix1,matrix2,len_of_row,len_of_col);
    
    return 0;
}