"""not done
Que12. Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
"""

try:
    value1 = int(input("Enter value1: "))
    value2 = int(input("Enter value2: "))
    res = value1/value2
    print(res)
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("Invalid value error")
