"""
Que30. Write a Python program to show method overriding.
"""

class Parent:

    def show(self):
        print("Hello from the Parent class!")

class Child(Parent):

    def show(self):
        super().show()
        print("Hello from the Child class!")

child = Child()
child.show()