"""
Que8. Write a Python program to write multiple strings into a file.
"""

strings = ["I am Ganesh\n",
        "I am taking IT training from TOPS Technologies\n",
        "Currently i am doing job in non IT field\n",
        "I stay in surat"]

f = open("test.txt","w")
for string in strings:
    f.write(string)
f.close()

print("All strings added successfully!")
    