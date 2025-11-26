bal=0.0
class Bank:
    def __init__(self,account_no,acc_holder):
        self.account_no=account_no
        self.acc_holder=acc_holder
    def deposit(self,amount):
        global bal
        bal+=amount
        print("Account No:",self.account_no)
        print("Account Holder:",self.acc_holder)
        print("Amount Deposited:",amount)
        print("Balance:",bal)

    def withdraw(self,amount):
        global bal
        if(bal<amount):
            print("Account No:",self.account_no)
            print("Account Holder:",self.acc_holder)
            print("Not enough balance to be withdrawn")
        else:
            bal-=amount
            print("Account No:",self.account_no)
            print("Account Holder:",self.acc_holder)
            print(f"Withdrawal of amount: {amount} successfull")
            print("Balance:",bal)

d1=Bank(1234,"Aratrika")
w1=Bank(2345,"Aratrika")

d1.deposit(2500)
w1.withdraw(300)
