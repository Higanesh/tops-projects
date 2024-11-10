"""
Que50. Write a Python function to check whether a number is perfect or not.
"""

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