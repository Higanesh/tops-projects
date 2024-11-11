"""done
Que64. Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
"""

specified_decimal_numbers = [1.25,3.14,2.65,0.45,7.35,0.99]
sorted_list = sorted(specified_decimal_numbers)
print(sorted_list)
print("maximum number from the specified decimal numbers list:",sorted_list[len(sorted_list)-1])
print("minimum number from the specified decimal numbers list:",sorted_list[0])


# However, you can make it simpler by using the built-in max() and min() functions
# print(max(specified_decimal_numbers))
# print(min(specified_decimal_numbers))


