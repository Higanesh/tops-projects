"""
Que23. Write a Python program to show multilevel inheritance.
"""

class grand_Parent_Class:

    def __init__(self,custId,dept):
        self.custId = custId
        self.dept = dept

    def showGrandParent(self):
        print("Grand Parent class called...")
        print(f"Customer Id: {self.custId}")
        print(f"Department: {self.dept}") 


class parent_Class(grand_Parent_Class):

    def __init__(self,custId,dept,name,age):
        super().__init__(custId,dept)
        self.name = name
        self.age = age

    def showParent(self):
        print("Parent class called...")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class child_Class(parent_Class):

    def __init__(self,custId,dept,name,age,email,mob):
        super().__init__(custId,dept,name,age)
        self.email = email
        self.mob = mob

    def showChild(self):
        print("Child class called...")
        print(f"Email: {self.email}")
        print(f"Mob No.: {self.mob}")

child_class = child_Class(1,'IT',"Ganesh",25,"ganesh@gmail.com",9657750872)

child_class.showGrandParent()

child_class.showParent()

child_class.showChild()

