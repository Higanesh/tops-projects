
def total_amt_in_bank(daily_initial_bal,daily_withdraw_amt,daily_deposite_amt):
    print("Today's initial balance: ",daily_initial_bal)
    print("Today's total withdrawal: ",daily_withdraw_amt)
    print("Today's total deposite: ",daily_deposite_amt)
    balance = (daily_initial_bal - daily_withdraw_amt) + daily_deposite_amt 
    print("Today's closing balance: ",balance)