"""
Que22. Write a Python program to check whether an element exists within a tuple. 
"""

nums = (56,89,78,15,49)
ele = int(input("Enter search element: "))
flag = 0
for num in range(0,len(nums)):
    if ele in nums:
        flag = 1

if flag == 1:
    print("Element is exist in tuple")
else:
    print("Element is not exist in tuple")



    