"""
Que29. Write a Python program to show method overloading.
"""

# class Math:

#     def add(self, a=0, b=0, c=0, d=0):
#         return a+b+c+d
    
# math = Math()

# print(math.add(5))
# print(math.add(5, 15))
# print(math.add(5, 15, 20))
# print(math.add(5, 15, 20, 30))


class Math:

    def add(self, *args):
        return sum(args)
    
math = Math()

print(math.add(5))
print(math.add(5, 15))
print(math.add(5, 15, 20))
print(math.add(5, 15, 20, 30))