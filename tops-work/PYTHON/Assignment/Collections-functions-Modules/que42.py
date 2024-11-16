"""done
Que42. Write a Python program to print all unique values in a dictionary.
"""

my_details = {
                
                "fname" : "Ganesh",
                "fname" : "Ganesh",
                "mname" : "Namdev",
                "mname" : "Namdev",
                "lname" : "Gayakwad",
                "lname" : "Gayakwad",
                "age" : 24,
                "age" : 24,
                "city" : "Surat",
                "city" : "Surat",
                "gender" : "Male",
                "gender" : "Male"
            }

print("All unique values in a dictionary",set(my_details.values()))


# empty_dict = {}
# unique_dict = {}

# for key in my_details:
#     if key in my_details:
#         empty_dict.update(my_details)
#         if key in empty_dict:
#             unique_dict.update(my_details)
# print(unique_dict)