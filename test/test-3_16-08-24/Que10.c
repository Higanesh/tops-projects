/*
10] Write a C program to count the frequency of each character in a given string.
*/

#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int freq[256] = {0};  // Array to store frequency of characters, initialized to 0
    int i;

    // Input string from user
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Count frequency of each character
    for(i = 0; str[i] != '\0'; i++) {
        freq[(int)str[i]]++;
    }

    // Display the frequency of each character
    printf("\nCharacter Frequency\n");
    for(i = 0; i < 256; i++) {
        if(freq[i] != 0) {
            printf("%c: %d\n", i, freq[i]);
        }
    }

    return 0;
}
