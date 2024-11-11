"""done
Que36. How Do You Check The Presence Of A Key In A Dictionary?
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
    print("Key is present in a dictionary")
else:
    print("Key is not present in a dictionary")