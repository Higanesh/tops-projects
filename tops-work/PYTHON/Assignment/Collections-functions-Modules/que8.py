"""done
Que8. Write a Python program to check a list is empty or not.
"""

user_input = input("Enter elements for list: ")
elements = user_input.split()
if len(elements) == 0:
    print("List is empty")
else:
    print("List is not empty")
