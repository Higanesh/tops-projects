
#include <stdio.h>

struct Employee {
    int empno;
    char empname[50];
    char address[100];
    int age;
};

int main() {
    struct Employee emp[5];

    for(int i = 1; i <= 5; i++){
        printf("Enter employee number %d details\n",i);
        printf("Enter Employee Number: ");
        scanf("%d", &emp[i].empno);
        printf("Enter Employee Name: ");
        scanf(" %s", emp[i].empname);
        printf("Enter Employee Address: ");
        scanf(" %s", emp[i].address);
        printf("Enter Employee Age: ");
        scanf("%d", &emp[i].age);
    }

    for(int i = 1; i <= 5; i++){
        printf("\nEmployee number %d Details:\n",i);
        printf("Employee Number: %d\n", emp[i].empno);
        printf("Employee Name: %s\n", emp[i].empname);
        printf("Employee Address: %s\n", emp[i].address);
        printf("Employee Age: %d\n", emp[i].age);
    }
    return 0;
}
