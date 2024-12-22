# Import necessary modules
from Banker import Banker  # Module for Banker-related operations
from Customer import Customer  # Module for Customer-related operations
import Exit  # Module to handle program exit

# Initialize the main menu loop
mm = True

# Start the program loop
while mm:
    # Display the main menu
    print("\n\t\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
    print("\t\tSelect your role\n")
    print("\t\t\t1) Banker\n\t\t\t2) Customer\n\t\t\t3) Exit")

    try:
        # Prompt the user to select a role
        role = int(input("Choose your role: "))

        # Check if the input is within the valid range
        if role in range(1, 4):
            if role == 1:
                # If user selects "Banker," call Banker.switch_case()
                mm = Banker.switch_case()
            elif role == 2:
                # If user selects "Customer," call Customer.switch_case()
                mm = Customer.switch_case()
            else:
                # If user selects "Exit," call Exit.exit()
                mm = Exit.exit()
        else:
            # If input is out of range, display an error message
            print("Please enter a value in the range 1-3")
    except ValueError:
        # Handle invalid input (e.g., non-integer values)
        print("Invalid Value, Please enter valid input")
