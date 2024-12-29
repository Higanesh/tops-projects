"""
Que26.  Write a Python program to show hybrid inheritance
"""

class A:

    def showA(self):
        print("Class A is called...")

class B(A):

    def showB(self):
        print("Class B is called...")

class C:

    def showC(self):
        print("Class C is called...")

class D(A,C):

    def showD(self):
        print("Class D is called...")

class E(B):

    def showE(self):
        print("Class E is called...")

# Single Inheritance

print("Single Inheritance")
b = B()
b.showA()
b.showB()

# Multiple Inheritance

print("Multiple Inheritance")
d = D()
d.showA()
d.showC()
d.showD()

# Multilevel Inheritance

print("Multilevel Inheritance")
e = E()
e.showA()
e.showB()
e.showE()