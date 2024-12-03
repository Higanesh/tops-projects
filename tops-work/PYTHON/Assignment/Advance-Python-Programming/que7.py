"""
Que7. Write a Python program to read the contents of a file and print them on the console.
"""

f = open("demo.txt","r")
data = f.read()
print(data)
f.close()