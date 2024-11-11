"""done
Que50. Write a Python function to check whether a number is perfect or not.
"""
# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. In other words, the sum of all divisors of the number, except the number itself, equals the number.
# example:
# 6: The divisors of 6 are 1, 2, and 3. 1 + 2 + 3 = 6.
def isPerfectNo(no):
    sum_Of_div = 0
    for divisior in range(1,no):
        if no % divisior == 0:
            sum_Of_div += divisior
    return sum_Of_div

real_no = int(input("Enter any number: "))
if real_no == isPerfectNo(real_no):
    print(f"{real_no} is PERFECT Number")
else:
    print(f"{real_no} is not PERFECT Number")