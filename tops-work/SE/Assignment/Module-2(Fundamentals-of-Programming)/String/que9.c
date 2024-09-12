/*
Que9. Write a program in C to find the maximum number of characters in a string.
*/

#include <stdio.h>
#include <string.h>

#define ASCII_SIZE 256 // Total number of ASCII characters

int main() {
    char str[1000];
    int freq[ASCII_SIZE] = {0}; // Array to store frequency of each character
    int maxFreq = 0;            // Variable to store the maximum frequency
    char maxChar;               // Variable to store the character with maximum frequency

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    // Remove the trailing newline character from fgets
    str[strcspn(str, "\n")] = 0;

    // Calculate frequency of each character
    for (int i = 0; str[i] != '\0'; i++) {
        freq[(int)str[i]]++;
    }

    // Find the character with the maximum frequency
    for (int i = 0; i < ASCII_SIZE; i++) {
        if (freq[i] > maxFreq) {
            maxFreq = freq[i];
            maxChar = (char)i;
        }
    }

    // Print the result
    printf("The character '%c' appears the most, with %d occurrences.\n", maxChar, maxFreq);

    return 0;
}
