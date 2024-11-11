"""done
Que28. Write a Python program to remove an empty tuple(s) from a list of tuples.
"""

tuple_list = [(1,2),(3,4),(5,6),(),(7,8),(9,10),(),(10,11),(11,12),()]
print(tuple_list)
for tpl in tuple_list:
    if (len(tpl)) == 0:
        tuple_list.remove(tpl)
print(tuple_list)