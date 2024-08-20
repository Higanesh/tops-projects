/*
15] Create a C program that finds the largest and smallest elements in a matrix.
*/

#include <stdio.h>

int main() {
    int rows, cols;
    int matrix[10][10];
    int i, j;
    int largest, smallest;

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

    // Initialize largest and smallest with the first element of the matrix
    largest = matrix[0][0];
    smallest = matrix[0][0];

    // Find the largest and smallest elements in the matrix
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            if (matrix[i][j] > largest) {
                largest = matrix[i][j];
            }
            if (matrix[i][j] < smallest) {
                smallest = matrix[i][j];
            }
        }
    }

    // Output the results
    printf("The largest element in the matrix is: %d\n", largest);
    printf("The smallest element in the matrix is: %d\n", smallest);

    return 0;
}
