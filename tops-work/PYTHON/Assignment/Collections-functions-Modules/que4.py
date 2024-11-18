"""
Que4. Write a Python function to get the largest number, smallest num and sum of all from a list.  
"""

def largest_num(ls):
    return max(ls)

def smallest_num(ls):
    return min(ls)

def sum_of_all(ls):
    return sum(ls)

sample_list = [4,6,2,9,3,-1]
print(f"Largest number in a list: {largest_num(sample_list)}")
print(f"Smallest number in a list: {smallest_num(sample_list)}")
print(f"Sum of all numbers in a list: {sum_of_all(sample_list)}")
