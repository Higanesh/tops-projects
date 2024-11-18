"""
Que46. Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})
"""

# Sample data
sample_data = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]

res = {}

# Iterate through the list of dictionaries
for ele in sample_data:
    item = ele['item']
    amount = ele['amount']

    # Add the amount to the existing value or initialize if not present
    if item not in res:
        res[item] = amount
    else:
        res[item] += amount

print(res) 



# another way to solve this problem

# from collections import Counter

# sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Counter = Counter()

# for ele in sample_data:
#     Counter[ele['item']] += ele['amount']
# print(Counter)




    



        
