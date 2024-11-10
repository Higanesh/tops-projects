""" done
Que6. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
"""

user_input = input("Enter elements for list: ")
string_ls = user_input.split()
counter = 0
for words in string_ls:
    if len(words) >= 2 and words[0] == words[-1]:
        counter += 1
print(counter)