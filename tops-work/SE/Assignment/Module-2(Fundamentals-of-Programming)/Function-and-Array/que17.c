/*
Que17. WAP to show difference between Structure and Union.
*/

#include <stdio.h>
#include <string.h>

// Define a structure
struct Person {
    char name[50];
    int age;
    float height;
};

// Define a union
union Data {
    int intValue;
    float floatValue;
    char charValue;
};

int main() {
    // Initialize and print structure members
    struct Person person1;
    strcpy(person1.name, "Alice");
    person1.age = 30;
    person1.height = 5.6;

    printf("Structure:\n");
    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);
    printf("Height: %.2f\n", person1.height);

    // Initialize and print union members
    union Data data1;
    
    data1.intValue = 10;
    printf("\nUnion (when storing intValue):\n");
    printf("intValue: %d\n", data1.intValue);
    
    data1.floatValue = 5.7;
    printf("floatValue: %.2f\n", data1.floatValue);
    
    data1.charValue = 'A';
    printf("charValue: %c\n", data1.charValue);

    // Print the value of intValue after storing charValue
    printf("intValue after storing charValue: %d\n", data1.intValue);

    return 0;
}
