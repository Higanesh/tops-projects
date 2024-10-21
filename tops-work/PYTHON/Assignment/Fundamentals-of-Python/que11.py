"""
Que11. Write a python program to sum of the first n positive integers. 
"""

sum = 0
for num1 in range(1,(int(input("Enter count: ")))+1):
    sum += num1
    num1 += 1
print(sum)
