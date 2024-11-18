"""
Que2. How will you remove last object from a list?
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

Ans-> To remove the last object from a list in Python, you can use the pop() method without any arguments. This method removes and returns the last element of the list.

list1[-1] refers to the last element of the list list1. Negative indexing allows you to access elements from the end of the list, where -1 is the last element, -2 is the second-to-last element, and so on.
"""

list1 = [2,33,222,14,25]
list1.pop()
print(list1)
print(list1[-1])

