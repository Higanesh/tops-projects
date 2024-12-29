"""
Que14. Write a Python program to handle exceptions in a calculator.
"""

class divisiorisgreaterthandividend(Exception):
    pass

try:
    value1 = int(input("Enter value1: "))
    value2 = int(input("Enter value2: "))

    print(f"Addition of value1 & value2: {value1+value2}")
    print(f"Multiplication of value1 & value2: {value1*value2}")

    if value2 > value1:
        raise divisiorisgreaterthandividend("value2 is greater than value1")
    else:
        print(f"Subtraction of value1 & value2: {value1-value2}")
        print(f"Division of value1 & value2: {value1/value2}")
        
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("Invalid value error")
except divisiorisgreaterthandividend as e:
    print(e)
    
