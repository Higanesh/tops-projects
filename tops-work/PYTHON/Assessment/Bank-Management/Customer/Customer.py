from Customer import withdraw
from Customer import deposite
from Customer import viewbal

class InsufficientAmount(Exception):
    pass

def switch_case():
    main_bal = 500
    while True:
        print("Welcome to Customers App")
        print("\tOperations Menu\n")
        print("\t1) Withdraw amt\n\t2) Deposite amt\n\t3) View balance\n\t4) Main Menu")
        try:
            value = int(input("Choose your role: "))             
        except ValueError:
            print("Invalid Value")
            continue
        if value in range(1,5):
            
            if value == 1:
                try:
                    w_input = int(input("Enter withdrawal amount: "))
                    if(w_input < main_bal):
                        main_bal = withdraw.withdraw_amount(main_bal,w_input)
                        print(f"{w_input}rs.is withdraw successfully,your remaining balance is {main_bal}")
                        print("Have a nice day")
                    else:
                        raise InsufficientAmount("insufficient amount")
                except InsufficientAmount as ia:
                    print(ia)
                    print("First check your account balance")
                
            elif value == 2:

                d_input = int(input("Enter deposite amount: "))
                main_bal = deposite.deposite_amount(main_bal,d_input)
                print(f"{d_input}rs.is deposite successfully,your remaining balance is {main_bal}")
                print("Have a nice day")

            elif value == 3:

                main_bal = viewbal.view_balance(main_bal)
                print(f"Account Balance: {main_bal}")
                print("Have a nice day")

            elif value == 4:
                return True
        else:
            print("please enter value in range")
