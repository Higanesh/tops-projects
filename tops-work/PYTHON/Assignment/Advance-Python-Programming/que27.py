"""
Que27.  Write a Python program to demonstrate the use of super() in inheritance.
"""

class parent_Class:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def showParent(self):
        print("Parent class called...")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class child_Class(parent_Class):

    def __init__(self,name,age,email,mob):
        super().__init__(name,age)
        self.email = email
        self.mob = mob

    def showChild(self):
        super().showParent()
        print("Child class called...")
        print(f"Email: {self.email}")
        print(f"Mob No.: {self.mob}")

child_class = child_Class("Ganesh",25,"ganesh@gmail.com",9657750872)
child_class.showChild()
