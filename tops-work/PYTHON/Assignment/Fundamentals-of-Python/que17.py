"""
Que17. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. 
"""

name1 = input("Enter first string: ")
name2 = input("Enter second string: ")
new_name1 = name2[0:2] + name1[2:]
new_name2 = name1[0:2] + name2[2:]
full_name = new_name1 + " " + new_name2
print(full_name)
