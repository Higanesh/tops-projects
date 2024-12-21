# Import specific functions from the Banker module
from Banker import addcust  # For adding customers
from Banker import viewcust  # For viewing customer details
from Banker import searchcust  # For searching a customer
from Banker import viewallcust  # For viewing all customer details
from Banker import totalamtinbank  # For calculating total amounts in the bank

# Function to handle Banker operations via a menu
def switch_case():
    """
    This function provides a menu for bankers to perform various operations 
    like adding customers, viewing customer details, and checking total amounts in the bank.
    """
    # Dictionary to store all customer details
    customers = {}
    
    while True:
        # Display the operations menu
        print("\n\t\tWelcome to Bankers App")
        print("\t\tOperations Menu\n")
        print("\t\t\t1) Add Customer\n\t\t\t2) View Customer\n\t\t\t3) Search Customer\n\t\t\t4) View all Customer\n\t\t\t5) Total amounts in Bank\n\t\t\t6) Main Menu")
        
        try:
            # Get user's choice from the menu
            value = int(input("Choose your role: "))             
        except ValueError:
            # Handle invalid input (non-integer values)
            print("Invalid Value, Please enter valid input")
            continue
        
        # Check if the entered value is within the valid range
        if value in range(1,7):
            if value == 1:
                # Add a customer
                all_customer_details = addcust.addcustomer(customers)

            elif value == 2:
                # View details of a specific customer by ID
                user_ip_for_view = int(input("Enter customer id for view: "))
                print(viewcust.viewcustomer(user_ip_for_view, all_customer_details))

            elif value == 3:
                # Search for a customer by ID
                try:
                    user_ip_for_search = int(input("Enter customer id for search: "))
                except ValueError:
                    print("Invalid customer id,Please enter valid customer id")
                print(searchcust.searchcustomer(user_ip_for_search, all_customer_details))

            elif value == 4:
                # View all customers and their details
                viewallcust.viewallcustomer(all_customer_details)

            elif value == 5:
                # Calculate the total amount in the bank
                try:
                    daily_initial_bal = int(input("Enter initial balance in bank: "))
                    daily_withdraw_amt = int(input("Enter withdrawal amount: "))
                    daily_deposite_amt = int(input("Enter deposit amount: "))
                except ValueError:
                    print("Invalid amount, Please enter valid amount")
                balance = totalamtinbank.total_amt_in_bank(daily_initial_bal, daily_withdraw_amt, daily_deposite_amt)
                print(f"Today's closing balance: {balance:.2f}")
            
            elif value == 6:
                # Return to the main menu
                return True
        else:
            # Handle invalid menu choice
            print("Please enter a value in the range 1-6")
