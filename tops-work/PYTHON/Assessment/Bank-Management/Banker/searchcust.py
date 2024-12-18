
def searchcustomer(cust_id,list_of_cust):
    for customer in list_of_cust:
        if customer.get("cust_id") == cust_id:
            print("Customer is availbale in bank")
            return customer
        else:
            pass

    print("Customer not found.")
        