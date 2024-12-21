
def viewallcustomer(list_of_cust):
    """
    This function displays the details of all customers in a formatted manner.
    """
    print("All customer details:\n")
    for customer in list_of_cust:
        print(f"Customer ID: {customer['cust_id']}, Name: {customer['name']}, Opening date: {customer["opening date"]}")

    # Iterate through the list of customers and print each customer's details
    if not list_of_cust:
        print("No customer details available.")
        return

