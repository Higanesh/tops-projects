"""
Que2. Write a Python program to get the Factorial number of given number.
for eg. factorial of 5
        5*4*3*2*1 = 120
"""

fact = 1
number = int(input("Enter any number: "))
for number in range(number,1,-1):
    fact *= number
    number = number - 1
print(fact)