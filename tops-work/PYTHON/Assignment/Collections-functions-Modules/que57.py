"""done
Que57. How will you randomizes the items of a list in place?
"""
# To randomize the items of a list in place means to shuffle or rearrange the order of elements in the list without creating a new list. The original list is modified directly, so the order of elements is randomized.

import random

items = [1,2,3,4,5]
random.shuffle(items)
print(items)