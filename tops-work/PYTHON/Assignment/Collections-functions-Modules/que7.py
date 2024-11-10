"""
Que7. Write a Python program to remove duplicates from a list. 
"""

user_input = input("Enter elements for list: ")
elements = user_input.split()
empty_ls = []
for element in elements:
    if element not in empty_ls:
        empty_ls.append(element)
print(empty_ls)


# you can use set also for this program
# empty_set = set()
# print(type(empty_set))
# for element in elements:
#     empty_set.add(element)
# print(empty_set)