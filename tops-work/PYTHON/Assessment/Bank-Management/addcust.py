import itertools

def addcustomer():
    list_of_cust = list()
    cust_id = itertools.count(start=1)

    # cust_id = input("Enter customer id: ")
    name = input("Enter customer name: ")
    age = int(input("Enter your age: "))
    acc_no = int(input("Enter your account number: "))
    address = input("Enter your address")
    cust = {
        "cust_id" : next(cust_id),
        "name" : name,
        "age" : age,
        "acc_no" : acc_no,
        "address" : address
    }
    
    list_of_cust.append(cust)
    print(list_of_cust)
