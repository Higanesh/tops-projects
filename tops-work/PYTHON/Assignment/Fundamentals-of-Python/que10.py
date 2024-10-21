"""
Que10. Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5. 
"""

num1 = int(input("Enetr 1st number: "))
num2 = int(input("Enetr 2nd number: "))
if num1 == num2 or (num1 + num2) == 5 or (num1 - num2) == 5:
    print(True)
else:
    print(False)