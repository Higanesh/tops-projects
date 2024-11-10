"""
Que31. How will you create a dictionary using tuples in python?
"""
# Tuple of tuples with (key, value) pairs
tuple_tpl = (("name","Ganesh"), ("age", 24), ("gender", 'M'), ("city", "surat"), ("mob no:", 9657750872))
dictionary = {}
dictionary.update(tuple_tpl)
print(dictionary)

# Using a for Loop to Create a Dictionary from Tuples

# for key,value in tuple_tpl:
#     dictionary[key] = value
# print(dictionary)