"""
Que13. Write a Python program to select an item randomly from a list. 
"""

import random

items_list = [1,2,3,4,5,6]
ele = int(input("Select random element: "))
if ele in items_list:
    print(ele)
else:
    print("Element is not available in list")  

# you can use random.choice method
# print(random.choice(items_list))
