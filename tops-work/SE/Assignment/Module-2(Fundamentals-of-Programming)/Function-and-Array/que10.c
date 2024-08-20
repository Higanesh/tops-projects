/*
Que10. WAP to perform Palindrome number using for loop and function
*/

#include <stdio.h>

// Function to check if a number is a palindrome
int isPalindrome(int num) {
    int originalNum = num;
    int reversedNum = 0;
    int remainder;
    
    // Reverse the number
    while (num != 0) {
        remainder = num % 10;
        reversedNum = reversedNum * 10 + remainder;
        num /= 10;
    }
    
    // Check if the reversed number is equal to the original number
    return (reversedNum == originalNum);
}

int main() {
    int number;
    
    // Input the number
    printf("Enter a number: ");
    scanf("%d", &number);
    
    // Check if the number is a palindrome
    if (isPalindrome(number)) {
        printf("%d is a palindrome.\n", number);
    } else {
        printf("%d is not a palindrome.\n", number);
    }
    
    return 0;
}
