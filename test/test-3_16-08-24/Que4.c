/*
4] Develop a C program that finds the transpose of a given matrix.
*/

#include <stdio.h>

int main() {
    int rows, cols;
    int matrix[10][10], transpose[10][10];
    int i, j;

    // Input the dimensions of the matrix
    printf("Enter the number of rows in the matrix: ");
    scanf("%d", &rows);
    printf("Enter the number of columns in the matrix: ");
    scanf("%d", &cols);

    // Input the elements of the matrix
    printf("Enter the elements of the matrix:\n");
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // Calculate the transpose of the matrix
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            transpose[j][i] = matrix[i][j];
        }
    }

    // Output the transpose
    printf("The transpose of the matrix is:\n");
    for (i = 0; i < cols; i++) {  // Notice the switch of rows and cols
        for (j = 0; j < rows; j++) {
            printf("%d ", transpose[i][j]);
        }
        printf("\n");
    }

    return 0;
}
