
import logging

# Configure the logging system
logging.basicConfig(
    filename='bank_operations.log',  # Log messages will be saved in this file
    level=logging.INFO,  # Log level (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of log messages
)

def total_amt_in_bank(daily_initial_bal, daily_withdraw_amt, daily_deposite_amt):
    """
    Calculates the total balance in the bank at the end of the day 
    based on the initial balance, total withdrawals, and total deposits.
    Includes input validation and logging.

    Args:
        daily_initial_bal (float or int): The initial balance in the bank at the start of the day.
        daily_withdraw_amt (float or int): The total amount withdrawn from the bank during the day.
        daily_deposite_amt (float or int): The total amount deposited into the bank during the day.

    Returns:
        float: The calculated closing balance, or None if inputs are invalid.
    """
    # Validate that all inputs are non-negative
    if daily_initial_bal < 0 or daily_withdraw_amt < 0 or daily_deposite_amt < 0:
        logging.error("Invalid input: Negative values provided.")
        print("Error: All values must be non-negative.")
        return

    # Log initial details
    logging.info(f"Initial Balance: {daily_initial_bal}, Withdrawals: {daily_withdraw_amt}, Deposits: {daily_deposite_amt}")

    # Display the daily bank details
    print(f"Today's initial balance: {daily_initial_bal:.2f}")
    print(f"Today's total withdrawal: {daily_withdraw_amt:.2f}")
    print(f"Today's total deposit: {daily_deposite_amt:.2f}")

    # Calculate the closing balance
    balance = (daily_initial_bal - daily_withdraw_amt) + daily_deposite_amt

    # Log the closing balance
    logging.info(f"Closing Balance: {balance}")

    # Return the calculated balance
    return balance

    