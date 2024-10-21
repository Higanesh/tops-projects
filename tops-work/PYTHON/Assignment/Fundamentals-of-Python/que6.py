"""
Que6. Write python program that swap two number with temp variable and
without temp variable. 
"""

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print("Before Swapping")
print("Number 1:",num1)
print("Number 2:",num2)
if num1 > 0 and num2 > 0:
    print("Enter 0 for using third variable and Enter 1 for without using third variable")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        temp = num1
        num1 = num2
        num2 = temp
    elif choice == 1:
        num1 = num1 + num2
        num2 = num1 - num2
        num1 = num1 - num2
    else:
        print("INVALID CHOICE")
print("After Swapping")
print("Number 1:",num1)
print("Number 2:",num2)