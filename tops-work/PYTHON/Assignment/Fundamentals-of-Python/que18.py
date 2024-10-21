"""
Que18. Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged. 
"""

name = input("Enter any string: ").lower()
if len(name) >= 3:
    if name.endswith("ing"):
        print(name + "ly")
    else:
        print(name + "ing")
else:
    print(name)