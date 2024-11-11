"""done
Que30. Write a Python program to convert a list of tuples into a dictionary.
"""

# List of tuples with (key, value) pairs
# 1st method by using update fuction
tuple_list = [("name","Ganesh"), ("age", 24), ("gender", 'M'), ("city", "surat"), ("mob no:", 9657750872)]
dict_obj = {}
dict_obj.update(tuple_list)
print(dict_obj)

# 2nd method by using dict object
# print(dict(tuple_list))


# 3rd method by using for loop
# for key,value in tuple_list:
#     dict_obj[key] = value
# print(dict_obj)