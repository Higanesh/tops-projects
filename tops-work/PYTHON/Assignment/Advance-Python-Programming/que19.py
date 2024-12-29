"""
Que19. Write a Python program to create a class and access the properties of the class using an object.
"""

class myDetails:
    name = "Ganesh"
    age = 25
    city = "Surat"
    branch = 'IT'

mydetails = myDetails()
print(f"My details is:\n{mydetails.name}\n{mydetails.age}\n{mydetails.city}\n{mydetails.branch}")