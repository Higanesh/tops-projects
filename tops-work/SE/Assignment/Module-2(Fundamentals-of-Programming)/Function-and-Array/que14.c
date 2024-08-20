/*
Que14. Perform 2D matrix array
*/

#include <stdio.h>

#define MAX 10 // Maximum size for matrix dimensions

// Function to input a matrix
void inputMatrix(int matrix[MAX][MAX], int rows, int cols) {
    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
}

// Function to display a matrix
void displayMatrix(int matrix[MAX][MAX], int rows, int cols) {
    printf("Matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

// Function to add two matrices
void addMatrices(int matrix1[MAX][MAX], int matrix2[MAX][MAX], int result[MAX][MAX], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
}

// Function to subtract two matrices
void subtractMatrices(int matrix1[MAX][MAX], int matrix2[MAX][MAX], int result[MAX][MAX], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = matrix1[i][j] - matrix2[i][j];
        }
    }
}

// Function to multiply two matrices
void multiplyMatrices(int matrix1[MAX][MAX], int matrix2[MAX][MAX], int result[MAX][MAX], int rows1, int cols1, int rows2, int cols2) {
    if (cols1 != rows2) {
        printf("Matrix multiplication is not possible.\n");
        return;
    }
    
    for (int i = 0; i < rows1; i++) {
        for (int j = 0; j < cols2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < cols1; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
}

int main() {
    int rows1, cols1, rows2, cols2;
    int matrix1[MAX][MAX], matrix2[MAX][MAX], result[MAX][MAX];
    
    // Input and display first matrix
    printf("Enter the number of rows and columns for the first matrix: ");
    scanf("%d %d", &rows1, &cols1);
    printf("Input matrix 1:\n");
    inputMatrix(matrix1, rows1, cols1);
    displayMatrix(matrix1, rows1, cols1);
    
    // Input and display second matrix
    printf("Enter the number of rows and columns for the second matrix: ");
    scanf("%d %d", &rows2, &cols2);
    printf("Input matrix 2:\n");
    inputMatrix(matrix2, rows2, cols2);
    displayMatrix(matrix2, rows2, cols2);
    
    // Addition
    if (rows1 == rows2 && cols1 == cols2) {
        addMatrices(matrix1, matrix2, result, rows1, cols1);
        printf("Matrix Addition:\n");
        displayMatrix(result, rows1, cols1);
    } else {
        printf("Matrix addition is not possible.\n");
    }
    
    // Subtraction
    if (rows1 == rows2 && cols1 == cols2) {
        subtractMatrices(matrix1, matrix2, result, rows1, cols1);
        printf("Matrix Subtraction:\n");
        displayMatrix(result, rows1, cols1);
    } else {
        printf("Matrix subtraction is not possible.\n");
    }
    
    // Multiplication
    if (cols1 == rows2) {
        multiplyMatrices(matrix1, matrix2, result, rows1, cols1, rows2, cols2);
        printf("Matrix Multiplication:\n");
        displayMatrix(result, rows1, cols2);
    } else {
        printf("Matrix multiplication is not possible.\n");
    }
    
    return 0;
}
