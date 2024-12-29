"""
Que9. Write a Python program to create a file and print the string into the file.
"""

file_name = "temp.txt"
string = "Tops Technologies IT Training Institute Vadodara"
with open(file_name,'w') as file:
    file.write(string)
print(f"String has been written to {file_name}")