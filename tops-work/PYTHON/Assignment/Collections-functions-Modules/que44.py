"""
Que44. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output:
ac ad bc bd
"""

# sample data
sample_data = {'1': ['a','b'], '2': ['c','d'], '3': ['e','f']}
common = list(sample_data.values())  # Get the list of all the value lists

# Iterate over the first list and combine it with elements from subsequent lists
for ele1 in common[0]:  # Loop through the first list
    for ele2 in common[1:]:  # Loop through the remaining lists
        for ele3 in ele2:  # Loop through each element of the current list
            print(f"{ele1}{ele3}",end=" ")


