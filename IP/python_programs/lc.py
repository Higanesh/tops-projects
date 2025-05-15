# import math
# a = [2,3,4,5]

# res = [int(math.pow(e,2)) for e in a]

# print(res)

# def func(*argv):
#     for arg in argv:
#         print(arg)

# func(1,2,3,4,5)

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

# this line shows dict comprehension here  
# d = { k:v for (k,v) in zip(keys, values)}  

# We can use below too
d = dict(zip(keys, values))  

print (d)