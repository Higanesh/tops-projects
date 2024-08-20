/*
Que3. WAP to find reverse of string using recursion
*/

#include <stdio.h>
#include <string.h>

// Function to reverse a string using recursion
void reverseString(char str[], int start, int end) {
    if (start >= end) {
        return;
    }
    // Swap characters at start and end
    char temp = str[start];
    str[start] = str[end];
    str[end] = temp;
    
    // Recursive call with updated indices
    reverseString(str, start + 1, end - 1);
}

int main() {
    char str[100];
    
    // Input the string
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Remove newline character if present
    size_t length = strlen(str);
    if (str[length - 1] == '\n') {
        str[length - 1] = '\0';
    }

    // Call the recursive function to reverse the string
    reverseString(str, 0, strlen(str) - 1);
    
    // Print the reversed string
    printf("Reversed string: %s\n", str);
    
    return 0;
}
