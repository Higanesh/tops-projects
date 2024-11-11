"""done
Que31. How will you create a dictionary using tuples in python?
"""
# Tuple of tuples with (key, value) pairs
# 1st method by using update fuction
tuple_tpl = (("name","Ganesh"), ("age", 24), ("gender", 'M'), ("city", "surat"), ("mob no:", 9657750872))
dictionary = {}
dictionary.update(tuple_tpl)
print(dictionary)

# 2nd method by using dict object
# print(dict(tuple_tpl))


# 3rd method by using for loop
# for key,value in tuple_tpl:
#     dictionary[key] = value
# print(dictionary)