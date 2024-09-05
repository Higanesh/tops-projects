/*
Que5. WAP to take two Array input from user and sort them in ascending or descending order as per user’s choice
*/

#include <stdio.h>

void sortArrayAcs(int arr[], int size) {
    int i, j, temp;
    for (i = 0; i < size - 1; i++) {
        for (j = i + 1; j < size; j++) {
            if (arr[i] > arr[j]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

void sortArrayDecs(int arr[], int size) {
    int i, j, temp;
    for (i = 0; i < size - 1; i++) {
        for (j = i + 1; j < size; j++) {
            if (arr[i] < arr[j]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}


int main() {
    
    int array1[20],array2[20];
    int temp,size1,size2,choice;
    printf("Enter no. of elements for array1\n");
    scanf("%d",&size1);
    printf("Enter first array elements\n");
    for(int i = 0; i < size1; i++)
    {
         scanf("%d",&array1[i]);
    }
    
    printf("Enter no. of elements for array2\n");
    scanf("%d",&size2);
    printf("Enter second array elements\n");
    for(int i = 0; i < size2; i++)
    {
         scanf("%d",&array2[i]);
    }
    
    printf("Enter 1 for ascending order or 2 for descending order:\n");
    scanf("%d", &choice);
    if(choice == 1){
        sortArrayAcs(array1, size1);
        printf("Sorted first array: ");
        printArray(array1, size1);
        
        sortArrayAcs(array2, size2);
        printf("Sorted second array: ");
        printArray(array2, size2);
    }else if(choice == 2){
        sortArrayDecs(array1, size1);
        printf("Sorted first array: ");
        printArray(array1, size1);
        
        sortArrayDecs(array2, size2);
        printf("Sorted second array: ");
        printArray(array2, size2);
    }else{
        printf("Invalid Choice");
    }
    return 0;
}