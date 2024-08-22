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
    struct Employee emp;

    // Input employee details
    printf("Enter Employee Number: ");
    scanf("%d", &emp.empno);
    printf("Enter Employee Name: ");
    scanf(" %[^\n]s", emp.empname); // to accept multi-word string
    printf("Enter Employee Address: ");
    scanf(" %[^\n]s", emp.address); // to accept multi-word string
    printf("Enter Employee Age: ");
    scanf("%d", &emp.age);

    // Display employee details
    printf("\nEmployee Details:\n");
    printf("Employee Number: %d\n", emp.empno);
    printf("Employee Name: %s\n", emp.empname);
    printf("Employee Address: %s\n", emp.address);
    printf("Employee Age: %d\n", emp.age);

    return 0;
}
