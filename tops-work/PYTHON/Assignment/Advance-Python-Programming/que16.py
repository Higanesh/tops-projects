"""
Que16. Write a Python program to handle file exceptions and use the finally block for closing
the file.
"""

filename = "example.txt"
try:
    file = open(filename,'r')
    value1 = int(input("Enter value1: "))
    value2 = int(input("Enter value2: "))
    res = value1/value2
    print(res)
    data = file.read()
    print(data,end="\n")
    file.close()
except FileNotFoundError:
    print("File not found")

except ZeroDivisionError:
    print("Division by zero error")

finally:
    print("Executing the finally block.")
