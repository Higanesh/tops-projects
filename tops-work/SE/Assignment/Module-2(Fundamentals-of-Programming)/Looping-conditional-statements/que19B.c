/*
A
B C
D E F
G H I J
K L M N O
*/

#include <stdio.h>

int main() {
    char ch = 'A';  // Starting character
    int n = 5;  // Number of rows
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= i; j++) {
            printf("%c ", ch);
            ch++;
        }
        printf("\n");
    }
    return 0;
}
