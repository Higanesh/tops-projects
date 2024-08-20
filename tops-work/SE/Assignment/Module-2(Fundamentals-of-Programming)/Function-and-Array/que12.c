/*
Que12. WAP to accept 5 students name and store it in array
*/

#include <stdio.h>

#define NUM_STUDENTS 5
#define NAME_LENGTH 50

int main() {
    char studentNames[NUM_STUDENTS][NAME_LENGTH];
    
    // Input names of 5 students
    printf("Enter the names of %d students:\n", NUM_STUDENTS);
    for (int i = 0; i < NUM_STUDENTS; i++) {
        printf("Student %d: ", i + 1);
        fgets(studentNames[i], NAME_LENGTH, stdin);
        
        // Remove the newline character from the input
        // fgets includes the newline character, so we need to remove it
        size_t len = strlen(studentNames[i]);
        if (len > 0 && studentNames[i][len - 1] == '\n') {
            studentNames[i][len - 1] = '\0';
        }
    }
    
    // Display the names of the students
    printf("\nThe names of the students are:\n");
    for (int i = 0; i < NUM_STUDENTS; i++) {
        printf("Student %d: %s\n", i + 1, studentNames[i]);
    }
    
    return 0;
}
