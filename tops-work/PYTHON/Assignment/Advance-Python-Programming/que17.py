"""
Que17.  Write a Python program to print custom exceptions.
"""
account_bal = 5000

class insufficientbalance(Exception):
    pass

try:
    withdraw_amt = float(input("Enter amount for withdraw: "))
    if withdraw_amt > account_bal:
        raise insufficientbalance("Insufficient balance")
    else:
        remaining_amt = account_bal - withdraw_amt
        print(f"Remaining balance: {remaining_amt}")
except insufficientbalance as e:
    print(e)
except ValueError:
    print("Invalid Value")
