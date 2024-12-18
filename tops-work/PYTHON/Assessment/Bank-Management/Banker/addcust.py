
def addcustomer(customers):
    list_of_cust = []
    while True:
        try: 
            cust_id = int(input("Enter customer id: "))
            name = input("Enter customer name: ")
            customers = {
                    "cust_id" : cust_id,
                    "name" : name,
                }
        except ValueError:
            print("invalid value")
            continue

        list_of_cust.append(customers)
        # print(list_of_cust)

        continue_input = input("Do you want to add another customer? (y for yes/n for no): ")
        if continue_input.lower() != 'y':
            return list_of_cust