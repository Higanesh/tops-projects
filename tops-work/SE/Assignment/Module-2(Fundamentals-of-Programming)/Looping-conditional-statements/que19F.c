/*
A 
A B 
A B C 
A B C D 
A B C D E 
*/

#include <stdio.h>

int main() {
    char c;
    int i, j;

    for(i = 1; i <= 5; i++) {
        c = 'A';
        for(j = 1; j <= i; j++) {
            printf("%c ", c);
            c++;
        }
        printf("\n");
    }

    return 0;
}
