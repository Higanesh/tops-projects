def viewcustomer(cust_id, list_of_cust):
    for customer in list_of_cust:
        if customer.get("cust_id") == cust_id:
            return customer
    print("Customer not found.")
    return None
