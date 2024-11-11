"""done
Que27. Write a Python program to find the repeated items of a tuple.
"""

tuple_obj = (1,2,3,4,3,5,3,2,8,9,7,5,4,6,1,5,4,9,7,5)
print("Original tuple elements: ",tuple_obj)
empty_list = []
repeated_list = []

for ele in tuple_obj:
    if ele not in empty_list:
        empty_list.append(ele)
    elif ele not in repeated_list:
        repeated_list.append(ele)
print("Repeated tuple elements: ",tuple(repeated_list))



# another solution by using set
# tuple_obj = (1, 2, 3, 4, 3, 5, 3, 2, 8, 9, 7, 5, 4, 6, 1, 5, 4, 9, 7, 5)
# unique_elements = set()    # Set to store unique elements
# repeated_list = []         # List to store repeated elements

# for ele in tuple_obj:
#     if ele not in unique_elements:
#         unique_elements.add(ele)  # Add to set if not seen before
#     elif ele not in repeated_list:
#         repeated_list.append(ele)  # Add to repeated list if not already present

# print("Repeated elements:", repeated_list)

