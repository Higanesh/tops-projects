"""done
Que48. Write a Python function to calculate the factorial of a number (a nonnegative integer)
"""

def factorial(num):
    fact = 1
    for num in range(num,1,-1):
        fact *= num
    return fact

no = int(input("Enter any number to calculate factorial: "))
print(f"Factorial of number {no} is: {factorial(no)}")