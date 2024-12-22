from datetime import datetime
from shared import balance

def addcustomer(customers):
    """
    This function allows the user to add customer details (customer ID and name).
    It collects the data and stores it in a list of dictionaries.
    
    Args:
        customers (dict): A dictionary to temporarily hold a single customer's details.

    Returns:
        list: A list containing dictionaries of all added customers.
    """
    # Initialize an empty list to store all customer details
    list_of_cust = []
    
    while True:
        try:
            # Get customer ID and name from user
            cust_id = int(input("Enter customer id: "))  # Input for customer ID (integer)
            name = input("Enter customer name: ")       # Input for customer name (string)
            opening_bal = float(input("Enter opening balance: ")) #Input for customer opening balance (float)
            # Get the current date and time
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create a dictionary for the current customer's details
            customers = {
                "cust_id": cust_id,
                "name": name,
                "opening date": current_datetime
            }

            balance[cust_id] = opening_bal  # Store balance using customer ID as key

        except ValueError:
            # Handle invalid input for customer ID (non-integer values)
            print("Invalid value, please enter a valid customer ID & opening balance.")
            continue

        # Append the customer's details dictionary to the list
        list_of_cust.append(customers)
        # Uncomment the following line to see the current state of the list while debugging
        # print(list_of_cust)

        # Ask if the user wants to add another customer
        continue_input = input("Do you want to add another customer? (y for yes/n for no): ")
        if continue_input.lower() != 'y':  # Exit the loop if the user does not input 'y'
            return list_of_cust  # Return the list of customers
