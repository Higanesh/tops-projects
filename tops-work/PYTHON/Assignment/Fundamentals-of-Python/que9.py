"""
Que9. Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero. 
"""

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if num1 == num2 or num2 == num3 or num3 == num1:
    sum = 0
else:
    sum = num1 + num2 + num3
print("Sum of three integer numbers: ",sum)