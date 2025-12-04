"""""16. Build a Student class storing id, name, and marks. Add methods to calculate grade.
class Student:
    def __init__(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks
    def grades(self):
        avg = sum(self.marks)/len(self.marks)
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"
s= Student(245,"Aratrika Debnath",[98,92,85])
print(s.grades())"""

"""17. Implement a Product → ElectronicProduct (inheritance) where Electronics adds warranty years.
class Product:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price
class Electronics(Product):
    def __init__(self,id,name,price,warranty_years):
        super().__init__(id,name,price)
        self.warranty_years = warranty_years
e= Electronics(765,"LAPTOP",50000,3)
print(f"{e.name} has a price of {e.price} and warranty of {e.warranty_years}yrs")"""

"""18. Create a Payment class with credit-card and UPI subclasses overriding process_payment().

class Payment():
    def __init__(self):
        pass
    def process_payment(self):
        print("Processing Payment .....")
class CreditCardPayment(Payment):
    def __init__(self):
        pass
    def process_payment(self):
        print("Credit Card Payment initiated")
class UPIPayment(Payment):
    def __init__(self):
        pass
    def process_payment(self):
        print("UPI Payment initiated")
c=CreditCardPayment()
c.process_payment()
upi=UPIPayment()
upi.process_payment()"""

"""19. Create a Vehicle class and Car, Bike subclasses. Override max_speed().

class Vehicle:
    def __init__(self):
        pass
    def max_speed(self):
        print("There is a max speed")
class Car(Vehicle):
    def __init__(self):
        pass
    def max_speed(self):
        print("The Max Speed is ",120,"kmph")
class Bike(Vehicle):
    def __init__(self):
        pass
    def max_speed(self):
        print("The Max Speed is ",150,"kmph")
cr= Car()
cr.max_speed()
bk = Bike()
bk.max_speed()"""

"""20. Implement Operator Overloading: add two objects of BankAccount to return total balance.

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def __add__(self,other):
        return self.balance + other.balance
a = BankAccount(100)
b= BankAccount(200)
print(a+b)"""

"""21.Build a ShoppingCart class implementing add, remove, total, apply_discount.

class shoppingcart:
    def __init__(self):
        self.items = []
    def add_item(self,name,price):
        self.items.append((name,price))
        print(name,"added to cart")
    def remove_item(self,name):
        for item in self.items:
            if item[0]==name:
                self.items.remove(item)
                print(name,"removed from cart")
                return
        print(name,"not in cart")
    def total_cost(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total
    def apply_discount(self,percent):
        total= self.total_cost()
        discount_amount=total*(percent/100)
        final_price=total-discount_amount
        return final_price
    def display_items(self):
        if not self.items:
            print("No items added to cart")
            return
        print("Items added to cart:")
        for name,price in self.items:
            print(name,"=",price)
cart=shoppingcart()
cart.add_item("Milk",100)
cart.add_item("carrot",60)
print()
cart.display_items()
print()
print("total cost:",cart.total_cost())
print("final price:",cart.apply_discount(100))
print()
cart.remove_item("carrot")
cart.display_items()"""

"""22. Create a Library class to store books and a method to search by title or author."""

class Library:
    def __init__(self):
        self.books = []
    def add_book(self,title,author):
        self.books.append({"title":title,"author":author})
    def search_book(self,query):
        return [bk for bk in self.books if query in (bk["title"],bk["author"])]
lib = Library()
lib.add_book("Archer's Voice","Mia Sheridan")
lib.add_book("The Edens","Devney Perry")
print(lib.search_book("Mia Sheridan"))


