/*
Que6. WAP to make addition, Subtraction and multiplication of two matrix using 2-D Array
*/

#include <stdio.h>

// Function to print a matrix
void printMatrix(int matrix[3][4], int rows, int cols) {
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

// Function to add two matrices
void addMatrices(int matrix1[3][4], int matrix2[3][4], int result[3][4], int rows, int cols) {
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            result[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
}

// Function to multiply two matrices element-wise
void multiplyMatrices(int matrix1[3][4], int matrix2[3][4], int result[3][4], int rows, int cols) {
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            result[i][j] = matrix1[i][j] * matrix2[i][j];
        }
    }
}

int main() {
    int matrix1[3][4] = {
        {1, 2, 3, 0},
        {4, 5, 6, 0},
        {7, 8, 9, 0}
    };

    int matrix2[3][4] = {
        {11, 22, 33, 0},
        {44, 55, 66, 0},
        {77, 88, 99, 0}
    };

    int rows = sizeof(matrix1) / sizeof(matrix1[0]);
    int cols = sizeof(matrix1[0]) / sizeof(matrix1[0][0]);

    int sumResult[3][4];
    int productResult[3][4];

    // Perform addition
    addMatrices(matrix1, matrix2, sumResult, rows, cols);
    
    // Perform multiplication
    multiplyMatrices(matrix1, matrix2, productResult, rows, cols);

    // Print matrices and results
    printf("Matrix-1:\n");
    printMatrix(matrix1, rows, cols);

    printf("Matrix-2:\n");
    printMatrix(matrix2, rows, cols);

    printf("Matrix-1 + Matrix-2:\n");
    printMatrix(sumResult, rows, cols);

    printf("Matrix-1 * Matrix-2 (Element-wise):\n");
    printMatrix(productResult, rows, cols);

    return 0;
}
