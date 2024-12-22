# Import necessary functions and classes from Customer module
from Customer_Operation import withdraw  # For withdrawal functionality
from Customer_Operation import deposite  # For deposit functionality
from Customer_Operation import viewbal   # For viewing account balance

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
            print("Invalid Value, Enter a valid input")  # Handle non-integer inputs
            continue

        # Check if the input is within the valid range
        if value in range(1, 5):
            # Handle withdrawal operation
            if value == 1:
                try:
                    cust_id = int(input("Enter customer ID: "))
                    # Get withdrawal amount from the user
                    w_input = int(input("Enter withdrawal amount: "))
                    updated_balance = withdraw.withdraw_amount(cust_id, w_input)
                    print(f"New balance after withdrawal: {updated_balance}")
    
                except ValueError as e:
                    print(e)

            # Handle deposit operation
            elif value == 2:
                # Get deposit amount from the user
                try:
                    cust_id = int(input("Enter customer ID: "))
                    d_input = int(input("Enter deposit amount: "))
                    updated_balance = deposite.deposite_amount(cust_id, d_input)
                    print(f"New balance after deposit: {updated_balance}")

                except ValueError as e:
                    print(e)
                
            # Handle balance view operation
            elif value == 3:
                try:
                    cust_id = int(input("Enter customer ID: "))
                    current_bal = viewbal.view_balance(cust_id)
                    print(f"Current balance for customer ID {cust_id}: {current_bal}")
                except ValueError as e:
                    print(e)
            # Handle returning to the main menu
            elif value == 4:
                return True  # Exit the customer menu and return to the main menu
        else:
            # Handle invalid menu choice
            print("Please enter a value in the range 1-4")
