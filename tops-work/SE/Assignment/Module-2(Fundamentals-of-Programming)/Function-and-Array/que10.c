/*
Que10. WAP to perform Palindrome number using for loop and function
*/

#include <stdio.h>

int isPalindrome(int num) {
    int originalNum = num;
    int reversedNum = 0;
    int remainder;
    
    while (num != 0) {
        remainder = num % 10;
        reversedNum = reversedNum * 10 + remainder;
        num /= 10;
    }
    
    return (reversedNum == originalNum);
}

int main() {
    int number;
    
    printf("Enter a number: ");
    scanf("%d", &number);
    
    if (isPalindrome(number)) {
        printf("%d is a palindrome.\n", number);
    } else {
        printf("%d is not a palindrome.\n", number);
    }
    return 0;
}
