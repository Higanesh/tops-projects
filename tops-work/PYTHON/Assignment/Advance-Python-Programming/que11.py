"""
Que11. Write a Python program to check the current position of the file cursor using tell().
"""

file_name = "temp.txt"

with open(file_name,'w') as f:
    f.write("This is temporary file to check cursor position in a file")
    cursor_pos = f.tell()
print(f"Cursor is at the {cursor_pos}th position")
