/*
Que12. Write a program in C to find the number of times a given word 'is' appears in the given string.
*/

#include <stdio.h>
#include <string.h>

int count_occurrences(char *str, const char *word) {
    int count = 0;
    char *pos = str;

    while ((pos = strstr(pos, word)) != NULL) {
        // Check if the word is isolated (not part of a longer word)
        if ((pos == str || *(pos - 1) == ' ') && (*(pos + strlen(word)) == ' ' || *(pos + strlen(word)) == '\0')) {
            count++;
        }
        pos += strlen(word);
    }
    
    return count;
}

int main() {
    char str[1000];
    const char *word = "is";
    int occurrences;

    // Input the string
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    
    // Remove the trailing newline character from fgets
    str[strcspn(str, "\n")] = 0;

    // Count occurrences of the word "is"
    occurrences = count_occurrences(str, word);

    // Output the result
    printf("The word '%s' appears %d times in the string.\n", word, occurrences);

    return 0;
}
