"""Exercise 8
Create a class BankAccount that supports deposit, withdraw, check balance, and displays
transaction logs."""

bal=0.0 #Balance
tl=[] #global transaction log
class Bank:
    def __init__(self,acc_no,acc_name):
        self.acc_no = acc_no
        self.acc_name = acc_name
    def deposit(self,amount):
        global bal
        global tl
        x=[]
        bal+=amount
        x.append("Deposit")
        x.append(amount)
        tl.append(x)
        print(f"Name: {self.acc_name},Account_no.: {self.acc_no}")
        print(f"Deposit of amount {amount} successful")
    def withdraw(self,amount):
        global bal
        global tl
        x=[]
        if amount > bal:
            print("Not enough money")
        else:
            bal-=amount
            x.append("Withdrawn")
            x.append(amount)
            tl.append(x)
            print(f"Name: {self.acc_name},Account_no.: {self.acc_no}")
            print(f"Withdrawal of amount {amount} successful")
    def balance(self):
        global bal
        print(f"Name: {self.acc_name},Account_no.: {self.acc_no}")
        print(f"Present Balance: {bal}")
    def transaction(self):
        global tl
        print(f"Name: {self.acc_name},Account_no.: {self.acc_no}")
        print(f"Transaction:{tl}")

obj1 = Bank(23457,"Aratrika Debnath")

obj1.deposit(50000)
obj1.withdraw(10000)
obj1.balance()
obj1.transaction()