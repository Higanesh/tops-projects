/*
5] Write a C program to merge two sorted arrays into a single sorted array.
*/

#include <stdio.h>

int main() {
    int arr1[50], arr2[50], merged[100];
    int size1, size2, i, j, k;

    // Input size of the first array
    printf("Enter the number of elements in the first sorted array: ");
    scanf("%d", &size1);
    printf("Enter %d elements of the first sorted array: ", size1);
    for(i = 0; i < size1; i++) {
        scanf("%d", &arr1[i]);
    }

    // Input size of the second array
    printf("Enter the number of elements in the second sorted array: ");
    scanf("%d", &size2);
    printf("Enter %d elements of the second sorted array: ", size2);
    for(i = 0; i < size2; i++) {
        scanf("%d", &arr2[i]);
    }

    // Merge the two sorted arrays
    i = 0; j = 0; k = 0;
    while(i < size1 && j < size2) {
        if(arr1[i] < arr2[j]) {
            merged[k++] = arr1[i++];
        } else {
            merged[k++] = arr2[j++];
        }
    }

    // Copy any remaining elements from the first array
    while(i < size1) {
        merged[k++] = arr1[i++];
    }

    // Copy any remaining elements from the second array
    while(j < size2) {
        merged[k++] = arr2[j++];
    }

    // Print the merged sorted array
    printf("The merged sorted array is: ");
    for(i = 0; i < size1 + size2; i++) {
        printf("%d ", merged[i]);
    }
    printf("\n");

    return 0;
}
