"""
Que13. Write a Python program to demonstrate handling multiple exceptions.
"""

class divisiorisgreaterthandividend(Exception):
    pass

try:
    value1 = int(input("Enter value1: "))
    value2 = int(input("Enter value2: "))
    if value2 > value1:
        raise divisiorisgreaterthandividend("value2 is greater than value1")
    else:
        res = value1/value2
        print(res)
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("Invalid value error")
except divisiorisgreaterthandividend as e:
    print(e)
    
