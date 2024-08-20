/*
16] Explain how typedef is used in C with an example.
*/

/*Ans: typedef is used to create new type names (aliases) for existing data types. This can help make code more readable, more portable, or simply reduce the amount of typing required when defining certain types repeatedly.
Syntax:
typedef existing_type new_type_name;

For eg.
#include <stdio.h>

typedef unsigned long int ULONG;  // Creating an alias for `unsigned long int`

int main() {
    ULONG a = 1000000;
    printf("Value of a: %lu\n", a);
    return 0;
}
*/ 