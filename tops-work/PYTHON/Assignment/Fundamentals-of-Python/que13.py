"""
Que13. Write a Python program to count the number of characters (character
frequency) in a string 
"""

name = input("Enter any string: ").lower()
empty_str = ''
for ch in name:
    if ch not in empty_str:
        empty_str += ch
        print(f"{ch} - {str(name.count(ch))}")