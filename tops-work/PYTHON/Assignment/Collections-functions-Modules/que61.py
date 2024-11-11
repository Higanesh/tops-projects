"""done
Que61. Write a Python program to calculate the area of a parallelogram
"""

# Area=b×h
def area_of_parallelogram(b,h):
    return b * h

base = float(input("Enter base of parallelogram: "))
height = float(input("Enter height of parallelogram: "))
print(area_of_parallelogram(base,height))