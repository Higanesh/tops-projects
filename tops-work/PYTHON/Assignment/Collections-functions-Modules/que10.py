"""
Que10. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30. 
"""

nums = range(1,31)
print(list(nums))
print(list(map(lambda num: num*num, nums))[:5])
print(list(map(lambda num: num*num, nums))[25:])
