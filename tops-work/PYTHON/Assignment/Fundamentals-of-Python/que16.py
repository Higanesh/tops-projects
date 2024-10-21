"""
Que16. Write a Python program to count the occurrences of each word in a
given sentence
"""

name = input("Enter any sentence: ").lower()
name_ls = name.split()
print(name_ls)
empty_ls = []
for word in name_ls:
    if word not in empty_ls:
        empty_ls.append(word)
        print(f"{word} - {name_ls.count(word)}") 