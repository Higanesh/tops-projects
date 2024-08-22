/*
Que18. Write a program of structure employee that provides the following
a.
information -print and display empno, empname, address and age
b.
Write a program of structure for five employee that provides the following information -print and display empno, empname, address and age
*/

#include <stdio.h>

// Define a structure for employee
struct Employee {
    int empno;
    char empname[50];
    char address[100];
    int age;
};

int main() {
    struct Employee emp[5];

    // Input employee details for 5 employees
    for(int i = 0; i < 5; i++) {
        printf("\nEnter details for Employee %d:\n", i+1);
        printf("Enter Employee Number: ");
        scanf("%d", &emp[i].empno);
        printf("Enter Employee Name: ");
        scanf(" %[^\n]s", emp[i].empname); // to accept multi-word string
        printf("Enter Employee Address: ");
        scanf(" %[^\n]s", emp[i].address); // to accept multi-word string
        printf("Enter Employee Age: ");
        scanf("%d", &emp[i].age);
    }

    // Display employee details for 5 employees
    printf("\nEmployee Details:\n");
    for(int i = 0; i < 5; i++) {
        printf("\nEmployee %d:\n", i+1);
        printf("Employee Number: %d\n", emp[i].empno);
        printf("Employee Name: %s\n", emp[i].empname);
        printf("Employee Address: %s\n", emp[i].address);
        printf("Employee Age: %d\n", emp[i].age);
    }

    return 0;
}
