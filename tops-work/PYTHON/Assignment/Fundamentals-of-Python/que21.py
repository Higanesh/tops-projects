"""
Que21. Write a Python function to reverses a string if its length is a multiple of
4. 
"""

name = input("Enter any string: ")
if len(name) % 4 == 0:
    print(name[::-1])
else:
    print("The length is not multiple of 4")
