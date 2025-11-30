"""26. Create a class Book with title, author, pages. Add method to check if pages > 300

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def pagechk(self):
        if self.pages >300:
            print("More than 300 pages")
        else:
            print("Less than 300 pages")

bk = Book("Archer's Voice", "Mia Sheridan", 435)
bk.pagechk()"""

"""27.Create a class BankAccount with deposit and withdraw methods.

bal=0.0
class Bank:
    def __init__(self,acc_name,acc_no):
        self.acc_name=acc_name
        self.acc_no=acc_no
    def deposit(self,amount):
        global bal
        bal+=amount
        print(f"Name: {self.acc_name},Account_no.: {self.acc_no}")
        print(f"Deposit of amount {amount} successful")
        print(f"Current balance: {bal}")
    def withdraw(self,amount):
        global bal
        if amount > bal:
            print("Not enough money")
        else:
            bal-=amount
            print(f"Name: {self.acc_name},Account_no.: {self.acc_no}")
            print(f"Withdrawal of amount {amount} successful")
            print(f"Current balance: {bal}")
bacc = Bank("Aratrika Debnath", 456372)
bacc.deposit(10000)
bacc.withdraw(1090)"""

"""28.Create a class Rectangle with methods to calculate area and perimeter.

class Rectangle:
    def __init__(self,colour,width,height):
        self.colour=colour
        self.width = width
        self.height = height
    def perimeter(self):
        print("Perimeter:",2*(self.width+self.height))
    def area(self):
        print("Area:",self.width*self.height)
r=Rectangle("red",4,5)
r.perimeter()
r.area()"""

"""29.  Create a class Student that stores marks of three subjects and calculates percentage.

class Student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def totalmarks(self):
        return self.m1+self.m2+self.m3
    def percentage(self):
        print("Name:",self.name)
        print("Percentage:",(self.totalmarks()/300)*100)
st= Student("Aratrika Debnath",99,98,97)
st.percentage()"""

"""30. Create a class Mobile with brand, model, and method to show details

class Mobile:
    def __init__(self,brand,model,colour):
        self.brand=brand
        self.model=model
        self.colour=colour
    def showdetails(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Colour: {self.colour}")
mb=Mobile("Samsung","s25 Ultra","Stardust")
mb.showdetails()"""