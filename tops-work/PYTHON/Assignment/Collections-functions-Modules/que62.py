"""
Que62. Write a Python program to calculate surface volume and area of a cylinder
"""

PI = 3.14

# V=πr^2h
def volume_of_cylinder(r,h):
    return round((PI * r * r * h),2)

# A=2πr^2+2πrh
def area_of_cylinder(r,h):
    return round(((2 * PI * r * r) + (2 * PI * r * h)),2)

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
print(volume_of_cylinder(radius,height))
print(area_of_cylinder(radius,height))