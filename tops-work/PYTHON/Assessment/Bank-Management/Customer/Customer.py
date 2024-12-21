# Import necessary functions and classes from Customer module
from Customer import withdraw  # For withdrawal functionality
from Customer import deposite  # For deposit functionality
from Customer import viewbal   # For viewing account balance

# Custom exception for handling insufficient balance
class InsufficientAmount(Exception):
    """
    Custom exception raised when a withdrawal exceeds the available balance.
    """
    pass

# Function to handle customer operations via a menu
def switch_case():
    """
    This function provides a menu for customers to perform operations like withdrawing,
    depositing, and viewing their account balance. It also handles exceptions and validates input.
    """

    # Infinite loop for menu-based interaction
    while True:
        # Display the operations menu
        print("Welcome to Customers App")
        print("\tOperations Menu\n")
        print("\t1) Withdraw amt\n\t2) Deposite amt\n\t3) View balance\n\t4) Main Menu")

        # Validate the user input for menu choice
        try:
            value = int(input("Choose your role: "))             
        except ValueError:
            print("Invalid Value")  # Handle non-integer inputs
            continue

        # Check if the input is within the valid range
        if value in range(1, 5):
            # Handle withdrawal operation
            if value == 1:
                try:
                    cust_id = int(input("Enter customer ID for withdrawal: "))
                    # Get withdrawal amount from the user
                    w_input = int(input("Enter withdrawal amount: "))

                    updated_balance = withdraw.withdraw_amount(cust_id, w_input)
                    print(f"New balance after withdrawal: {updated_balance}")
                    # Check if the withdrawal amount is within the available balance
                    # if w_input < main_bal:
                    #     main_bal = withdraw.withdraw_amount(main_bal, w_input)  # Perform withdrawal
                    #     print(f"{w_input}rs. is withdrawn successfully, your remaining balance is {main_bal}")
                    #     print("Have a nice day")
                    # else:
                    #     # Raise custom exception if the amount exceeds balance
                    #     raise InsufficientAmount("Insufficient amount")
                except InsufficientAmount as ia:
                    print(ia)  # Display error message for insufficient funds
                    print("First check your account balance")

            # Handle deposit operation
            elif value == 2:
                # Get deposit amount from the user
                try:
                    cust_id = int(input("Enter customer ID for deposit: "))
                    d_input = int(input("Enter deposit amount: "))
                    updated_balance = deposite.deposite_amount(cust_id, d_input)
                    print(f"New balance after deposit: {updated_balance}")
                except ValueError:
                    print("Invalid amount, Please enter valid amount")
                # main_bal = deposite.deposite_amount(main_bal, d_input)  # Perform deposit
                # print(f"{d_input}rs. is deposited successfully, your remaining balance is {main_bal}")
                # print("Have a nice day")

            # Handle balance view operation
            elif value == 3:
                cust_id = int(input("Enter customer id to view balance: "))
                current_bal = viewbal.view_balance(cust_id)
                print(f"Current balance for customer ID {cust_id}: {current_bal}")
                # main_bal = viewbal.view_balance(main_bal)  # View current account balance
                # print(f"Account Balance: {main_bal}")
                # print("Have a nice day")

            # Handle returning to the main menu
            elif value == 4:
                return True  # Exit the customer menu and return to the main menu
        else:
            # Handle invalid menu choice
            print("Please enter a value in the range 1-4")
