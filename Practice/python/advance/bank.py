
class InsufficientAmtException(Exception):
    def __init__(self):
        print("Insufficient balance")
        pass

class bank:
    bal = 0
    def __init__(self):
        pass

    def get_balance(self):
        print("Your current balance is: ",self.bal)

    def deposite(self,amt):
        self.bal = self.bal + amt

    def withdraw(self,amt):
        if amt > self.bal:
            raise InsufficientAmtException(amt - self.bal)
        else:
            self.bal = self.bal - amt

b = bank()
b.get_balance()
b.deposite(5000)
b.get_balance()
try:
    b.withdraw(10000)
except Exception:
    pass

b.get_balance()