
class MyException(Exception):
    print("Insufficient balance")
    pass

withdraw_amt = int(input("Enter withdraw amt"))
bal = 5000

try :
    if bal < withdraw_amt :
        raise MyException()
    else :
        pass
except MyException:
    print("err")
else:
    print(f"remaining balance: {bal - withdraw_amt}")