"""
Que10. Write a Python program to read a file and print the data on the console.
"""

file_name = "test.txt"

with open(file_name,'r') as file:
    data = file.read()
print(data)
