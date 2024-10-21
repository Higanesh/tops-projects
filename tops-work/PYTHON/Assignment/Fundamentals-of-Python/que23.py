"""
Que23. Write a Python function to insert a string in the middle of a string. 
"""

name = input("Enter any string: ")
name_ls = name.split()
# name_ls.insert(int(len(name_ls)/2),input("Enter center string: "))
name_ls.insert(int(input("Enter index: ")),input("Enter center string: "))
result = " ".join(name_ls)
print(result)
