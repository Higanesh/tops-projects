/*
Que21. Accept 3 numbers from user using while loop and check each numbers palindrome
*/

#include <stdio.h>

int isPalindrome(int num) {
    int original_num = num, reversed_num = 0;
    while (num != 0) {
        int digit = num % 10;
        reversed_num = reversed_num * 10 + digit;
        num /= 10;
    }
    return original_num == reversed_num;
}

int main() {
    int num, count = 0;
    while (count < 3) {
        printf("Enter number %d: ", count + 1);
        scanf("%d", &num);

        if (isPalindrome(num)) {
            printf("%d is a palindrome.\n", num);
        } else {
            printf("%d is not a palindrome.\n", num);
        }
        count++;
    }
    return 0;
}
