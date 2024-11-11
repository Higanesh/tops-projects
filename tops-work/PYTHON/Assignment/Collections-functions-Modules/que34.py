"""done
Que34. Write a Python script to check if a given key already exists in a dictionary.
"""

my_details = {
                "fname" : "Ganesh",
                "mname" : "Namdev",
                "lname" : "Gayakwad",
                "age" : 24,
                "city" : "Surat",
                "gender" : "Male"
            }
key = input("Enter key for search: ")
if key in my_details:
    print("Key already exist in a dictionary")
else:
    print("Key does not exist in a dictionary")