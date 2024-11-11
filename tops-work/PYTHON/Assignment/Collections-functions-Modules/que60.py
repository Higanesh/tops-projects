"""done
Que60. Write a Python program to calculate the area of a trapezoid
"""

# Area= 1/2×(a+b)×h
def area_of_trapezoid(a,b,h):
    return (1/2 * (a + b) * h)

base1 = float(input("Enter base1 for trapezoid: "))
base2 = float(input("Enter base2 for trapezoid: "))
height = float(input("Enter height for trapezoid: "))
print(area_of_trapezoid(base1,base2,height))