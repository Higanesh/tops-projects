"""
Que19. Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
"""

name = input("Enter any string: ")
sub_str1 = "not"
sub_str2 = "poor"
print("first appearance of 'not'",name.index("not"))
print("first appearance of 'poor'",name.index("poor"))
if (name.index("poor") - name.index("not")) == 4:
    new_name = name[0:name.index("not")] + "good" + name[(name.index("poor") + 4):]
    print(new_name)
else:
    print(name)