# customer/withdraw.py
from shared import balance  # Import the shared balance dictionary

def withdraw_amount(cust_id, amount):
    """
    Deducts the withdrawal amount from the balance.
    """
    if cust_id not in balance:
        raise ValueError("Customer ID not found.")
    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative.")
    if amount > balance[cust_id]:
        raise ValueError("Insufficient balance.")
    
    balance[cust_id] -= amount  # Update balance
    return balance[cust_id]  # Return the updated balance
