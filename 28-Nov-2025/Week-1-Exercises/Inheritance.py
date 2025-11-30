"""34.Create parent class Vehicle and child class Car that overrides a method start().
class Vehicle:
    def __init__(self):
        pass
    def start(self):
        print("Vehicles are may or may not need a key or other mechanisms to start")
class Car(Vehicle):
    def __init__(self):
        pass
    def start(self):
        print("The Modern Cars start with the push of a button placed beside the steering wheel.")
cr= Car()
cr.start()"""

"""35. . Create Person → Employee → Manager (multilevel). Add different methods in each

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self,name,age,location,join_date):
        super().__init__(name,age)
        self.location = location
        self.join_date = join_date
    def salary(self):
        print(f"Employee {self.name} in location: {self.location} has a salary of Rs.4.8 LPA")
class Manager(Employee):
    def __init__(self,name,age,location,join_date,department):
        super().__init__(name,age,location,join_date)
        self.department = department
    def details(self):
        print(f"Manager {self.name} in department: {self.department} has an incremented salary of Rs.15 LPA")
m = Manager("Aratrika",22,"Kolkata","27-Oct-2025","Emerging Tech")
m.display()
m.salary()
m.details()"""

"""36. Create a base class Payment and child classes: CreditCardPayment and UPIPayment. Override
 process()

class Payment():
    def __init__(self):
        pass
    def method(self):
        print("Processing Payment .....")
class CreditCardPayment(Payment):
    def __init__(self):
        pass
    def method(self):
        print("Credit Card Payment initiated")
class UPIPayment(Payment):
    def __init__(self):
        pass
    def method(self):
        print("UPI Payment initiated")
c=CreditCardPayment()
c.method()
upi=UPIPayment()
upi.method()"""

"""37. Create two parent classes Camera and Phone, and a child class SmartPhone (multiple
 inheritance)

class Camera():
    def __init__(self,megapixel):
        self.megapixel = megapixel
class Phone():
    def __init__(self,type,model):
        self.type = type
        self.model = model
class SmartPhone(Phone,Camera):
    def __init__(self,type,model,cam):
        Phone.__init__(self,type,model)
        Camera.__init__(self,cam)
smp = SmartPhone("Touch Screen",236,50)
print(f"Smart Phone type {smp.type} and model {smp.model} with a {smp.megapixel} megapixel camera")"""


