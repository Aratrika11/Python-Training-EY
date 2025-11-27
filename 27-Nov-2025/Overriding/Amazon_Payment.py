class Payment:
    def pay(self,name,amount,account_code):
        if self.checker(account_code,amount):
            print("Payment Successful")
        else:
            print("Payment Failed")
    def checker(self,account_code,amount):
        if amount < 100:
            return False
        else:
            return True
class GooglePay(Payment):
    def pay(self,name,amount,account_code):
        if self.checker(account_code,amount):
            print("Payment Successful through Gpay")
        else:
            print("Payment Failed")
class PhonePay(Payment):
    def pay(self,name,amount,account_code):
        if self.checker(account_code,amount):
            print("Payment Successful through PhonePay")
        else:
            print("Payment Failed")
class PayTm(Payment):
    def pay(self,name,amount,account_code):
        if self.checker(account_code,amount):
            print("Payment Successful through PayTm")
        else:
            print("Payment Failed")

print("How do you want to pay ?")
n=int(input("Enter 1 for Google Pay \n Enter 2 for Phone Pay \n Enter 3 for PayTm "))
if n==1:
    cust = GooglePay()
    cust.pay("Aratrika",500,"123")
elif n==2:
    cust = PhonePay()
    cust.pay("Aratrika",500,"Ad456")
elif n==3:
    cust = PayTm()
    cust.pay("Aratrika",500,"pytm34")
else:
    print("Payment Method not Supported")