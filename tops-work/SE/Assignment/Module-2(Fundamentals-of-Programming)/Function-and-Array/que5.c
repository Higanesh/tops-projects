/*
Que5. WAP to take two Array input from user and sort them in ascending or descending order as per user’s choice
*/

#include <stdio.h>

// Function to perform the sorting
void sortArray(int arr[], int size, int ascending) {
    int i, j, temp;
    for (i = 0; i < size - 1; i++) {
        for (j = i + 1; j < size; j++) {
            if ((ascending && arr[i] > arr[j]) || (!ascending && arr[i] < arr[j])) {
                // Swap elements
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int size1, size2;
    int choice;
    
    // Input size and elements of the first array
    printf("Enter the number of elements in the first array: ");
    scanf("%d", &size1);
    int arr1[size1];
    
    printf("Enter the elements of the first array:\n");
    for (int i = 0; i < size1; i++) {
        scanf("%d", &arr1[i]);
    }
    
    // Input size and elements of the second array
    printf("Enter the number of elements in the second array: ");
    scanf("%d", &size2);
    int arr2[size2];
    
    printf("Enter the elements of the second array:\n");
    for (int i = 0; i < size2; i++) {
        scanf("%d", &arr2[i]);
    }
    
    // Input the sorting order
    printf("Enter 1 for ascending order or 2 for descending order:\n");
    scanf("%d", &choice);
    int ascending = (choice == 1);
    
    // Sort and print the first array
    sortArray(arr1, size1, ascending);
    printf("Sorted first array: ");
    printArray(arr1, size1);
    
    // Sort and print the second array
    sortArray(arr2, size2, ascending);
    printf("Sorted second array: ");
    printArray(arr2, size2);
    
    return 0;
}
