# customer/viewbal.py
from shared import balance  # Import the shared balance dictionary

def view_balance(cust_id):
    """
    Retrieves and returns the balance for a specific customer.

    Args:
        cust_id (int): The ID of the customer whose balance is to be viewed.

    Returns:
        float: The current balance of the customer.

    Raises:
        ValueError: If the customer ID is not found in the system.
    """
    if cust_id not in balance:
        raise ValueError("Customer ID not found.")
    
    # Return the balance for the given customer ID
    return balance[cust_id]
