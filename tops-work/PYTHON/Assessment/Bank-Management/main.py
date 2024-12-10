import Banker
import Customer
import Exit

# def switch_case(value):
#             switch_dict = {
#                 1: Banker.switch_case(),
#                 2: Customer.switch_case(),
#                 3: Exit.exit()
#             }
#             return switch_dict.get(value, "please enter value in range")

print("WELCOME TO PYTHON BANK MANAGEMENT SYSTEM")
print("Select your role")
print("1) Banker\n2) Customer\n3) Exit")

try:
    role = int(input("Choose your role: "))
    if role in range(1,4):
        if role == 1:
            print("Welcome to Bankers App")
            print("Operations Menu")
            print("1) Add Customer\n2) View Customer\n3) Search Customer\n4) View all Customer\n5) Total amounts in Bank")

            try:
                bank_op = int(input("Choose your role: "))
                print(Banker.switch_case(bank_op))
                
            except ValueError:
                print("Invalid Value")

            print("Bank Testing...")
        elif role == 2:
            print("Welcome to Customers App")
            print("Operations Menu")
            print("1) Withdraw amt\n2) Deposite amt\n3) View balance")

            try:
                cust_op = int(input("Choose your role: "))
                print(Customer.switch_case(cust_op))
                
            except ValueError:
                print("Invalid Value")

            print("Cust. Testing...")
        else:
            Exit.exit()
    # print(switch_case(role))
    else:
        print("please enter value in range")
except ValueError:
    print("Invalid Value")

print("Main Testing...")