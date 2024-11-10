"""
Que29. Write a Python program to unzip a list of tuples into individual lists.
"""

tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (10, 11), (11, 12)]
for tpl in tuple_list:
    print(list(tpl),end=",")