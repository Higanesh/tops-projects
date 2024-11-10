"""
Que14. Write a Python program to find the second smallest number in a list.
"""

user_input = input("Enter list elements: ")
nums = [int(num) for num in user_input.split()]
empty_nums = sorted(nums)
print(empty_nums)
second_smallest_num = empty_nums[1]
print(second_smallest_num)
        
        
