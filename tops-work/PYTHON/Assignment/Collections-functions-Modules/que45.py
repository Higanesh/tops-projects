"""done
Que45. Write a Python program to find the highest 3 values in a dictionary
"""

nums = {'v1':52,'v2':25,'v3':47,'v4':12,'v5':97,'v6':67,'v7':5}
print("Original list of values: ",nums.values())
if len(nums) >= 3:
    print("Highest 3 values in a dictionary: ",(sorted(nums.values(),reverse=True))[:3])
else:
    print("Dictionary does not have enough element to perform this operation")


    # print("Original list of values: ",list(nums.values()))
    # sorted_set = sorted(list(nums.values()),reverse=True)
    # print("Sorted list of values: ",sorted_set)
    # print("Highest 3 values in a dictionary: ",sorted_set[0:3])