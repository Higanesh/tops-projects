"""done
Que32. Write a Python script to sort (ascending and descending) a dictionary by value.
"""

dict_obj = {
            "no1":65,
            "no2":24,
            "no3":34,
            "no4":23,
            "no5":97
            }
print("Original dictionary: ",dict_obj)

# lambda item: item[1]: This is an anonymous function that takes a single argument, item.

# item: In this case, each item is a key-value pair (a tuple) from the dictionary. For example, ("no1", 65), ("no2", 24), etc.

# item[1]: This extracts the second element of the tuple, which is the value (e.g., 65, 24, 34). Using item[1] as the key means the sorting will be based on the dictionary values rather than the keys.

sorted_dict_asc = dict(sorted(dict_obj.items(),key=lambda item: item[1],reverse = False))
sorted_dict_desc = dict(sorted(dict_obj.items(),key=lambda item: item[1],reverse = True))
print("Sorted dictionary in ascending order: ",sorted_dict_asc)
print("Sorted dictionary in descending order: ",sorted_dict_desc)


