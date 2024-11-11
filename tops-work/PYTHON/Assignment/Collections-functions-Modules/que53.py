"""done
Que53. How can you pick a random item from a list or tuple?
"""

import random

items_list = [4,2,9,1,6,3]
items_tpl = (4,2,9,1,6,3)

print(random.choice(items_list))
print(random.choice(items_tpl))