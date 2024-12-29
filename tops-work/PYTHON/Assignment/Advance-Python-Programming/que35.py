"""
Que35. Write a Python program to search for a word in a string using re.search().
"""

import re

word = "learning"
string = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a batteries included language due to its comprehensive standard library.Guido van Rossum began working on python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as python 0.9.0.python 2.0 was released in 2000. python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. python 2.7.18, released in 2020, was the last release of python 2.python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning python community."

result = re.search(word,string)
print(result)
