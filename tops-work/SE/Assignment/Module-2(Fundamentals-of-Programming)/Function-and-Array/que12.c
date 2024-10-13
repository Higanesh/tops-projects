/*
Que12. WAP to accept 5 students name and store it in array
*/

#include <stdio.h>
#include <string.h>

int main() {
    
    int row = 5;
    int col = 50;
    char studentNames[row][col];
    
    printf("Enter the names of %d students:\n", row);
    for (int i = 0; i < row; i++) {
        printf("Student %d: ", i + 1);
        fgets(studentNames[i], col, stdin);
        int len = strlen(studentNames[i]);
        if (len > 0 && studentNames[i][len - 1] == '\n') {
            studentNames[i][len - 1] = '\0';
        }
    }
    printf("\nThe names of the students are:\n");
    for (int i = 0; i < row; i++) {
        printf("Student %d: %s\n", i + 1, studentNames[i]);
    }
    return 0;
}

