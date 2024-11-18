"""
Que33. Write a Python script to concatenate following dictionaries to create a new one.
"""

person_info = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "phone_numbers": "9657750872"
}

product_details = {"id": 101, "name": "Laptop", "price": 999.99, "quantity": 25}

temp_ls = [person_info,product_details]

new_one_dict = {}

for le in temp_ls:
    new_one_dict.update(le)
print(new_one_dict)



# another version for duplicate values:

# for le in temp_ls:
#     for key, value in le.items():
#         if key in new_one_dict:
#             # If key already exists in the new dictionary, store both values in a list
#             if isinstance(new_one_dict[key], list):
#                 new_one_dict[key].append(value)
#             else:
#                 new_one_dict[key] = [new_one_dict[key], value]
#         else:
#             # If key doesn't exist, just add it
#             new_one_dict[key] = value
# print(new_one_dict)
