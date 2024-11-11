"""done
Que19. Write a Python program to create a tuple with different data types.
"""
#There are three ways to create tuple in python

#Using the tuple() Constructor with a List
tuple_obj1 = tuple([1, "ganesh", 3.50, "sagar", 's', 'g', 12 + 25j, 10]) 

#Using Parentheses to Define a Tuple
tuple_obj2 = (1, "ganesh", 3.50, "sagar", 's', 'g', 12 + 25j, 10
) 

#Creating a Tuple Without Parentheses (Comma-Separated Values)
comma_tuple_obj = 1, "ganesh", 3.50, "sagar", 's', 'g', 12 + 25j, 10 

print("Obj1 Type: ",type(tuple_obj1))
print("Obj1 Elements: ",tuple_obj1)
print("Obj2 Type: ",type(tuple_obj2))
print("Obj2 Elements: ",tuple_obj2)
print("Obj3 Type: ",type(comma_tuple_obj))
print("Obj3 Elements: ",comma_tuple_obj)

    