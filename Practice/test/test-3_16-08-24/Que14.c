/*
14] Write a C program to reverse the words in a given sentence without using any library
functions.
*/

#include <stdio.h>
#include <string.h>

void reverseWord(char* start, char* end) {
    while (start < end) {
        char temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

void reverseWordsInSentence(char* sentence) {
    char *wordStart = NULL;
    char *temp = sentence;

    // Reverse each word in the sentence
    while (*temp) {
        if (wordStart == NULL && (*temp != ' ' && *temp != '\0')) {
            wordStart = temp;
        }
        if (wordStart && (*(temp + 1) == ' ' || *(temp + 1) == '\0')) {
            reverseWord(wordStart, temp);
            wordStart = NULL;
        }
        temp++;
    }

    // Reverse the entire sentence to get the words in the right order
    reverseWord(sentence, temp - 1);
}

int main() {
    char sentence[100];

    // Input the sentence
    printf("Enter a sentence: ");
    fgets(sentence, sizeof(sentence), stdin);

    // Remove the newline character at the end
    int len = strlen(sentence);
    if (sentence[len - 1] == '\n') {
        sentence[len - 1] = '\0';
    }

    // Reverse the words in the sentence
    reverseWordsInSentence(sentence);

    // Output the result
    printf("Reversed sentence: %s\n", sentence);

    return 0;
}
