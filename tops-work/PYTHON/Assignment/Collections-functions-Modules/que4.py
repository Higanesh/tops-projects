"""
Que4. Write a Python function to get the largest number, smallest num and sum of all from a list.  
"""


# max_num = num_list[0]
# for num in num_list:
#     if max_num > num:
#         continue
#     else:
#         max_num = num
# print(max_num)






def largest(num_list):
    max_num = num_list[0]
    for num in num_list:
        if max_num > num:
            continue
        else:
            max_num = num
    print(max_num)

user_input = input("Enter elements for list: ")
num_ls = user_input.split()
largest(num_ls)

# # def smallest:


# # def sumOfAllElements:
# num_ls = [1,2,3]
# largest(num_ls)