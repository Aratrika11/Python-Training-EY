"""31.Create a class Employee with constructor and method to print details.
class Employee:
    def __init__(self,name,role,age,joining,salary):
        self.name = name
        self.role = role
        self.age = age
        self.joining = joining
        self.salary = salary
    def showdetails(self):
        print(f"Name: {self.name}\nRole: {self.role}\nAge: {self.age}\nJoining: {self.joining}\nSalary: {self.salary}")
emp = Employee("Aratrika Debnath","ASE",22,"27th October 2025",4.8)
emp.showdetails()"""

"""32.Create a class Temperature with constructor and methods to convert Celsius to Fahrenheit and
 vice versa.

class Temperature():
    def __init__(self,temp):
        self.temp = temp
    def celsiusToFahrenheit(self):
        return (self.temp*9/5)+32
    def fahrenheitToCelsius(self):
        return (self.temp-32)*5/9
    def display(self,n):
        if n==1:
            print(f"Farenheit: {self.celsiusToFahrenheit()}")
        elif n==2:
            print(f"Celsius: {self.farenheitToCelsius()}")
t = Temperature(10)
n=int(input("Enter 1 if you want the temperature from Celcius to Fahrenheit and 2 for vice versa: "))
t.display(n)"""

"""33. Create a class Laptop with constructor taking brand, RAM, price, and method to calculate
 discount.

class Laptop():
    def __init__(self,brand,RAM,price):
        self.brand = brand
        self.RAM = RAM
        self.price = price
    def discount(self):
        pr=self.price*(1-0.65)
        print("Price after 65% discount: ",int(pr))
lp = Laptop("Samsung","64",89000)
lp.discount()"""
