"""
Que12. Write a Python program to calculate the length of a string. 
"""

name = input("Enter any name: ")
# print(len(name))  #inbuild method is also available for count length of string
counter = 0
for ch in name:
    counter += 1
print(counter)