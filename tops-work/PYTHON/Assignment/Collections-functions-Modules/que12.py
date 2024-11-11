"""done
Que12. Write a Python program to convert a list of characters into a string. 
"""

user_input = input("Enter list of characters: ")
char_list = user_input.split()
print(char_list)
name = "".join(char_list)
print(name) 