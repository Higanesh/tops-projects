"""
Que35. How Do You Traverse Through A Dictionary Object In Python?
Ans->

Here are the most common ways to traverse a dictionary:

1. Iterating Over Keys (Default Iteration)

    # Sample dictionary
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}

    # Iterate over keys
    for key in my_dict:
        print(key)

2. Iterating Over Keys Using keys() Method

    # Iterate over keys using keys() method
    for key in my_dict.keys():
        print(key)

3. Iterating Over Values Using values() Method

    # Iterate over values using values() method
    for value in my_dict.values():
        print(value)

4. Iterating Over Key-Value Pairs Using items() Method

    # Iterate over key-value pairs using items() method
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
"""


