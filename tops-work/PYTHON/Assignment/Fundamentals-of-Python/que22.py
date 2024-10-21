"""
Que22. Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string. 
"""

main_str = input("Enter any string: ")                     
empty_str = ""
# no_of_char = int(input("Enter character count: "))
str_len = len(main_str) 
if str_len < 2:
    print(empty_str)
else:
    print(main_str[0:2] + main_str[(str_len - 2):str_len])





    # if you want to get last 2 chars in reverse order

    # print(main_str[0:2] + main_str[(str_len - (str_len + 1)):(str_len - (str_len + 3)):-1])

    # get a string made of the first n and the last n chars from a given a string. 

    # print(main_str[0:no_of_char] + main_str[(str_len - no_of_char):str_len])
    # print(main_str[0:no_of_char] + main_str[(str_len - (str_len + 1)):(str_len - (str_len + (no_of_char + 1))):-1])