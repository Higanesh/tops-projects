"""
Que16. Write a Python program to check whether a list contains a sub list
"""

main_list = [1,2,3,[4,5,6],7,8]
print("Main list: ",main_list)
flag = 0
for ele in main_list:
    if isinstance(ele,list):
         flag = 1
         print("Sublist: ",list(ele))

if flag == 1:
    print("Sublist is available")
else:
    print("Sublist is not available")
