"""
Que30. Write a Python program to convert a list of tuples into a dictionary.
"""

# List of tuples with (key, value) pairs
tuple_list = [("name","Ganesh"), ("age", 24), ("gender", 'M'), ("city", "surat"), ("mob no:", 9657750872) ]
dictionary = {}
dictionary.update(tuple_list)
print(dictionary)