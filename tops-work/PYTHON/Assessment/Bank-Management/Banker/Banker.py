from Banker import addcust 
from Banker import viewcust 
from Banker import searchcust 
from Banker import viewallcust 
from Banker import totalamtinbank

def switch_case():
    customers = {}
    while True:
        print("\n\t\tWelcome to Bankers App")
        print("\t\tOperations Menu\n")
        print("\t\t\t1) Add Customer\n\t\t\t2) View Customer\n\t\t\t3) Search Customer\n\t\t\t4) View all Customer\n\t\t\t5) Total amounts in Bank\n\t\t\t6) Main Menu")
        try:
            value = int(input("Choose your role: "))             
        except ValueError:
            print("Invalid Value")
            continue
        
        if value in range(1,7):
            if value == 1:
                all_customer_details = addcust.addcustomer(customers)
                
            elif value == 2:
                user_ip_for_view = int(input("Enter cust id for view: "))
                print(viewcust.viewcustomer(user_ip_for_view,all_customer_details))

            elif value == 3:
                user_ip_for_search = int(input("Enter cust id for view: "))
                print(searchcust.searchcustomer(user_ip_for_search,all_customer_details))

            elif value == 4:
                viewallcust.viewallcustomer(all_customer_details)

            elif value == 5:
                daily_initial_bal = int(input("Enter initial balance in bank: "))
                daily_withdraw_amt = int(input("Enter withdrawal amount: "))
                daily_deposite_amt = int(input("Enter deposite amount: "))
                totalamtinbank.total_amt_in_bank(daily_initial_bal,daily_withdraw_amt,daily_deposite_amt)
            elif value == 6:
                return True
        else:
            print("please enter value in range")

