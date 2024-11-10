"""
Que9. Write a Python function that takes two lists and returns true if they have at least one common member. 
"""

def common_member(list1,list2):
    for ele in list1:
        if ele in list2:
            return True
    return False


user_input1 = input("Enter list elements: ")
user_input2 = input("Enter list elements: ")
list1 = user_input1.split()
list2 = user_input2.split()
print(common_member(list1,list2))
