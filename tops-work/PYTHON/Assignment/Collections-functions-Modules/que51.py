"""done
Que51. Write a Python function that checks whether a passed string is palindrome or not
"""

def isPalindrom(real_str):
    rev_str = real_str[::-1]
    if rev_str == real_str:
        print("String is PALINDROM")
    else:
        print("String is not PALINDROM")

passed_str = input("Enter string for check palindrom: ")
isPalindrom(passed_str)
