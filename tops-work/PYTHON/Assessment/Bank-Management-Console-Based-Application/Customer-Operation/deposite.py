# customer/deposite.py
from shared import balance  # Import the shared balance dictionary

def deposite_amount(cust_id, amount):
    """
    Adds the deposit amount to the balance.
    """
    if cust_id not in balance:
        raise ValueError("Customer ID not found.")
    if amount < 0:
        raise ValueError("Deposit amount cannot be negative.")
    
    balance[cust_id] += amount  # Update balance
    return balance[cust_id]  # Return the updated balance
