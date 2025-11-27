bal=0.0
tl=[]
class Bank:
    def __init__(self,acc_name,acc_no):
        self.acc_name=acc_name
        self.acc_no=acc_no
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


class SavingsAccount(Bank):
    def __init__(self,name,acc_no,branch,annual_interest_rate: float=0.05):
        super().__init__(name,acc_no)
        #super().__init__(acc_no)
        self.branch=branch
        self.annual_interest_rate = annual_interest_rate
    def interest(self,mnth):
        global bal
        if mnth<12:
            interest=bal* self.annual_interest_rate/12
            print(f"Name: {self.acc_name},Account_no.: {self.acc_no}, Interest: {interest}")
        else:
            interest=bal* self.annual_interest_rate
            print(f"Name: {self.acc_name},Account_no.: {self.acc_no}, Interest: {interest}")
cust = SavingsAccount("Aratrika",23456,"Lake Town")
cust.deposit(50000)
cust.interest(20)
cust.transaction()