"""
Que20. Write a Python program to demonstrate the use of local and global variables in a class.
"""

# Global variable
global_variable = 25

class MyClass:

    def __init__(self):
        pass

    def localScope(self):
        # Local variable: Exists only within this method
        local_variable = 15
        print(f"Local variable is: {local_variable}")
        
        # Accessing the global variable
        print(f"Accessing global variable inside the method: {global_variable}")

# Create an object of the class
my_class = MyClass()

# Call the method to demonstrate local scope
my_class.localScope()

# Accessing the global variable outside the class
print(f"Global variable outside the class is: {global_variable}")
