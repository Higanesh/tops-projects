
import re

# nameAndage = "ganesH is 24 and Sagar is 25, Manish is 23 and Rupesh is 26"

# age = re.findall(r'\d{1,3}',nameAndage)
# print(age)
# name = re.findall(r'[A-Za-z0-9]',nameAndage)
# print(name)
# names = re.findall(r'[a-z][A-Z]',nameAndage)
# print(names)

flag = re.search("i","sakshi is registered in python programming")
print(flag)

if re.search("i","sakshi is registered in python programming"):
    print("found")
else:
    print("not found")

fan = re.match()