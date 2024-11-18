"""
Que37. Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
"""

dict_of_nums = {12:"ganesh",1:"sagar",6:"manish",19:"rupesh",35:"chetan",40:"nayan"}
print(f"Original dictionary: \n{dict_of_nums}")
new_dict = {}
for key in dict_of_nums.keys():
    if key in range(1,16):
        new_dict[key] = dict_of_nums[key]
print("Dictionary where the keys are numbers between 1 and 15: ")
print(new_dict)

