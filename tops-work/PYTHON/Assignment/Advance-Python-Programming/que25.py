"""
Que25. Write a Python program to show hierarchical inheritance.
"""

class Parent:
    
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def showParent(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")

class Child1(Parent):

    def __init__(self, id, name, age, email):
        super().__init__(id, name)
        self.age = age
        self.email = email

    def showChild1(self):
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

class Child2(Parent):

    def __init__(self, id, name, phone, dept):
        super().__init__(id, name)
        self.phone = phone
        self.dept = dept

    def showChild2(self):
        print(f"Phone Number: {self.phone}")
        print(f"Department: {self.dept}")

child1 = Child1(1,"Ganesh",25,"ganesh@gmail.com")
child1.showParent()
child1.showChild1()

child2 = Child2(1,"Sagar",9657750872,'IT')
child2.showParent()
child2.showChild2()


        