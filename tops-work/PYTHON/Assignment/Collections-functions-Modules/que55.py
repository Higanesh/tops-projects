"""
Que55. How can you get a random number in python?
"""

# you can generate random numbers using the random module. This module provides various functions to generate random numbers of different types, including integers, floats, and numbers from a specific range or distribution.

import random

print(random.randint(1000,9999))
print(round(random.random(),2))
print(random.randrange(10000,99999))