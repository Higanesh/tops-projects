"""done
Que38. Write a Python program to check multiple keys exists in a dictionary
"""

flag = False
my_details = {
                "fname" : "Ganesh",
                "mname" : "Namdev",
                "lname" : "Gayakwad",
                "age" : 24,
                "city" : "Surat",
                "gender" : "Male"
            }
keys_to_check = ["name", "age"]

# Check if all keys in keys_to_check are present in my_details
if all(key in my_details for key in keys_to_check):
        flag = True

if flag:
    print("All keys are available")
else:
    print("All keys are not available")