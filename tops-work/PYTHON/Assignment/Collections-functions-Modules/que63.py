"""done
Que63. Write a Python program to returns sum of all divisors of a number
"""

def sumOfDivisiors(num):
    divisiors = []
    for divisior in range(1,(num+1)):
        if num % divisior == 0:
            divisiors.append(divisior)
    print(divisiors)
    return sum(divisiors)

num = int(input("Enter any number: "))
print(sumOfDivisiors(num))

    