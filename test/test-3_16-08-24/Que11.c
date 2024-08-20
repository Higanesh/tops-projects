/*
11] Create a C program that reads an array of integers from the user and removes duplicate
elements from the array.
*/

#include <stdio.h>

int main() {
    int arr[100], uniqueArr[100];
    int size, i, j, k;
    int isUnique;

    // Input the size of the array
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    // Input elements in the array
    printf("Enter %d elements: ", size);
    for(i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    // Remove duplicates
    k = 0;
    for(i = 0; i < size; i++) {
        isUnique = 1;
        for(j = 0; j < k; j++) {
            if(arr[i] == uniqueArr[j]) {
                isUnique = 0;
                break;
            }
        }
        if(isUnique) {
            uniqueArr[k] = arr[i];
            k++;
        }
    }

    // Display the array without duplicates
    printf("Array after removing duplicates: ");
    for(i = 0; i < k; i++) {
        printf("%d ", uniqueArr[i]);
    }
    printf("\n");

    return 0;
}
