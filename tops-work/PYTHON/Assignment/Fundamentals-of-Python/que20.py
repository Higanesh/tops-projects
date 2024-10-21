"""
Que20. Write a Python function that takes a list of words and returns the length
of the longest one. 
"""

user_input = input("Enter elements separated by space: ")
words = user_input.split()
index = 0
max = len(words[0])
for index in range(index,len(words)):
    print(words[index],":",len(words[index]))
    if len(words[0]) < len(words[index]):
        max = len(words[index])
print("The length of the longest word is",max)

