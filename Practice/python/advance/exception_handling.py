
# def test():
#     try:
#         a = int(input("Enter any number: "))
#         print(a)
#         return True
#     except:
#         print("Please enter valid integer number")
#         return False
#     finally:
#         print("Print Something...")


# print(test())


# a = 10
# try:
#     b = a/0
#     print(b)
# except ZeroDivisionError:
#     print("your divisor is zero")
# finally:
#     print("Finally Block...")


try:
    a = int(input("Enter any number: "))
    print(a)
    b = a/0
    print(b)
except ZeroDivisionError:
    print("your divisor is zero")
except ValueError:
    print("Enter valid integer number")
finally:
    print("Finally Block...")

