"""
Que47. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string. Sample string: 'w3resource'
Expected output:
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""

sample_string = "w3resource"
empty_dict = {}

empty_str = []
for st in sample_string:
    if st not in empty_str:
        empty_str.append(st)
        empty_dict[st] = sample_string.count(st)
print(empty_dict)


# type 2
# for st in sample_string:
#     empty_dict[st] = sample_string.count(st)
# print(empty_dict)

# type 3
# from collections import Counter

# sample_string = "w3resource"
# empty_dict = dict(Counter(sample_string))
# print(empty_dict)




   