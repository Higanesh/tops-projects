"""done
Que39. Write a Python script to merge two Python dictionaries
"""

my_details1 = {
                "fname" : "Ganesh",
                "mname" : "Namdev",
                "lname" : "Gayakwad"
            }

my_details2 = {
                "age" : 24,
                "city" : "Surat",
                "gender" : "Male"
            }

my_details1.update(my_details2)
print(my_details1)

# merged_details = {**my_details1, **my_details2}
# print(merged_details)