/*
11] Explain the difference between ++x and x++ in C with an example.
*/

/*Ans: the increment operators ++x (pre-increment) and x++ (post-increment) are used to increase the value of a variable by one.
Difference Between ++x and x++:
Pre-Increment (++x): Increments the value of 'x' first, then returns the incremented value.
Post-Increment (x++): Returns the current value of 'x' first, then increments the value of 'x'.
*/

#include <stdio.h>

int main() {
    int x = 5;
    int y, z;

    y = ++x;
    printf("After pre-increment:\n");
    printf("x = %d, y = %d\n", x, y);

    x = 5;

    z = x++;  
    printf("After post-increment:\n");
    printf("x = %d, z = %d\n", x, z);  

    return 0;
}
