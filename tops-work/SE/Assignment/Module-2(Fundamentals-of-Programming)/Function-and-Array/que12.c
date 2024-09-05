/*
Que12. WAP to accept 5 students name and store it in array
*/

#include <stdio.h>
#include <string.h>

int main() {
    
    int NUM_STUDENTS = 5;
    int NAME_LENGTH = 50;
    char studentNames[NUM_STUDENTS][NAME_LENGTH];
    
    printf("Enter the names of %d students:\n", NUM_STUDENTS);
    for (int i = 0; i < NUM_STUDENTS; i++) {
        printf("Student %d: ", i + 1);
        fgets(studentNames[i], NAME_LENGTH, stdin);
        int len = strlen(studentNames[i]);
        if (len > 0 && studentNames[i][len - 1] == '\n') {
            studentNames[i][len - 1] = '\0';
        }
    }
    printf("\nThe names of the students are:\n");
    for (int i = 0; i < NUM_STUDENTS; i++) {
        printf("Student %d: %s\n", i + 1, studentNames[i]);
    }
    return 0;
}

