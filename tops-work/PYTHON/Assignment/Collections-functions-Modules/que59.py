"""
Que59. Write a Python program to convert degree to radian
"""

import math

# Radians=Degrees×π/180
def degree_to_radian(degree):
    return degree * (math.pi / 180)

degrees = float(input("Enter degrees: "))
print(f"{degrees} degrees = {degree_to_radian(degrees):.4f} radians")
