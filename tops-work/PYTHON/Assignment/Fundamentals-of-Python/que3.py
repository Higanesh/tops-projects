"""
Que3. Write a Python program to get the Fibonacci series of given range. 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 
"""

first = 0
second = 1
for n in range(int(input("Enter limit for fibonacci series: "))):
   print(first,end=" ")
   next = first + second
   first = second
   second = next