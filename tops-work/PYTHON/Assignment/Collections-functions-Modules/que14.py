"""done
Que14. Write a Python program to find the second smallest number in a list.
"""

user_input = input("Enter list elements: ")
nums = [int(num) for num in user_input.split()]
sorted_nums = sorted(set(nums))
if len(sorted_nums) >= 2:
    print(f"Sorted List {sorted_nums}")
    second_smallest_num = sorted_nums[1]
    print(f"Second Smallest Number is: {second_smallest_num}")
else:
    print("Please enter more than 2 numbers in a list")    
        
