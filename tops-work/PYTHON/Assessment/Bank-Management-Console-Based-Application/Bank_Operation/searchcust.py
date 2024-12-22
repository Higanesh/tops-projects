def searchcustomer(cust_id, list_of_cust):
    """
    Searches for a customer by their ID in a list of customer dictionaries.

    Args:
        cust_id (int): The ID of the customer to search for.
        list_of_cust (list): A list containing dictionaries where each dictionary represents a customer's details.

    Returns:
        dict: The dictionary containing the customer's details if found.
        None: If no customer with the given ID is found or if the customer list is empty.
    """
    # Iterate through the list of customers to find a match
    for customer in list_of_cust:
        if customer.get("cust_id") == cust_id:  # Check if the customer's ID matches the given ID
            print("Customer is available in the bank.")  # Notify that the customer exists
            return customer  # Return the matching customer's details
    
    # Handle case where the list of customers is empty
    if not list_of_cust:
        print("No customers available to search.")  # Notify that the list is empty
        return None

    # Notify that the customer was not found in the list
    print("Customer not found.")
    return None  # Explicitly return None if no match is found
