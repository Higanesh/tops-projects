"""
Que36. Write a Python program to match a word in a string using re.match().
"""

import re

word = "python"
string = "Python is a high-level, general-purpose programming language."

result = re.match(word,string,re.IGNORECASE)
print(result)