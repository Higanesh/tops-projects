"""
Que26. Write a Python program to replace last value of tuples in a list.
"""

tuple_obj = (15,56,87,45,67) # Step 1: Create a tuple
print("Original Tuple:",tuple_obj)
list_obj = list(tuple_obj) # Step 2: Convert the tuple to a list

# Step 3: Modify the last element in the list
list_obj[(len(list_obj)-1)] = 76

# Step 4: Convert the list back to a tuple and print it
print("Tuple after replacing last value:",tuple(list_obj))
