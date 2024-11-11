"""
Que37. Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
"""

dict_of_nums = {12:"ganesh",1:"sagar",6:"manish",19:"rupesh",35:"chetan",40:"nayan"}
empty_dict = {}
for key in dict_of_nums.keys():
    if key in range(1,15):
        empty_dict.update(dict_of_nums[key])
print(empty_dict)

