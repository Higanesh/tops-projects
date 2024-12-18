from Banker import Banker
from Customer import Customer
import Exit
mm = True
while mm:
    print("\n\t\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
    print("\t\tSelect your role\n")
    print("\t\t\t1) Banker\n\t\t\t2) Customer\n\t\t\t3) Exit")

    try:
        role = int(input("Choose your role: "))
        if role in range(1,4):
            if role == 1:
                mm = Banker.switch_case()
            elif role == 2:
                mm = Customer.switch_case()
            else:
                mm = Exit.exit()
        else:
            print("please enter value in range")
    except ValueError:
        print("Invalid Value")