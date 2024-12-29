"""
Que24. Write a Python program to show multiple inheritance.
"""

class Parent1:

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def showParent1(self):
        print("Parent1 class called...")
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")


class Parent2:
    def __init__(self,email,phone):
        self.email = email
        self.phone = phone

    def showParent2(self):
        print("Parent2 class called...")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone}")

class child(Parent1,Parent2):
    def __init__(self, dept, id, name,email,phone):
        Parent1.__init__(self,id, name)
        Parent2.__init__(self,email,phone)
        self.dept = dept

    def showChild(self):
        print("Child class called...")
        print(f"Department: {self.dept}")

childObj = child('IT',1,"Ganesh","ganesh@gmail.com",9657750872)
childObj.showParent1()
childObj.showParent2()
childObj.showChild()



        