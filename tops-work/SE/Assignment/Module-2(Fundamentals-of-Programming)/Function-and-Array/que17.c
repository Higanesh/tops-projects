/*
Que17. WAP to show difference between Structure and Union.
*/

#include <stdio.h>
#include <string.h>

struct Person {
    char name[50];
    int age;
    float height;
};

union Data {
    int Value1;
    float Value2;
    char Value3;
};

int main() {
    
    struct Person person1;
    strcpy(person1.name, "Ganesh");
    person1.age = 24;
    person1.height = 5.2;

    printf("Structure:\n");
    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);
    printf("Height: %.2f\n", person1.height);

    union Data data1;
    
    data1.Value1 = 10;
    printf("Integer Value: %d\n", data1.Value1);
    
    data1.Value2 = 5.7;
    printf("Float Value: %.2f\n", data1.Value2);
    
    data1.Value3 = 'A';
    printf("Character Value: %c\n", data1.Value3);

    return 0;
}
