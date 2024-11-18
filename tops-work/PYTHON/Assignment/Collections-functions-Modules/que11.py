"""
Que11. Write a Python function that takes a list and returns a new list with unique elements of the first list. 
"""

def unique_elements(elements_list,unique_elements_list):
    for element in elements_list:
        if element not in unique_elements_list:
            unique_elements_list.append(element)
    print(unique_elements_list)

elements_list = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
unique_elements_list = []
unique_elements(elements_list,unique_elements_list)

# Alternative Solution Using set
# You can achieve the same result more efficiently by using a set, which automatically removes duplicates:

# elements_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
# unique_elements_list = list(set(elements_list))
# print(unique_elements_list)
