"""
Que15. Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
"""

filename = "example.txt"
try:
    with open(filename,'r') as f:
        value1 = int(input("Enter value1: "))
        value2 = int(input("Enter value2: "))
        res = value1/value2
        print(res)
        data = f.read()
        print(data,end="\n")
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Division by zero error")