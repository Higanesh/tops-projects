"""
Que40. Write a Python program to map two lists into a dictionary 
"""

# Two lists
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

# Convert two lists into a dictionary using zip() and dict()
result = dict(zip(keys, values))

# Output the resulting dictionary
print(result)


  
