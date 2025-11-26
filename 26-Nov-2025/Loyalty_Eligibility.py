"""Exercise 7
Create a class Customer with attributes name, age, city. Add a method that checks if the
customer is eligible for a loyalty program (age &gt; 25)."""

class Customer:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def loyalty(self):
        if self.age>25:
            print(f"Customer: {self.name},Age: {self.age},is eligible")
        else:
            print(f"Customer: {self.name},Age: {self.age},is not eligible")

obj2 = Customer("Aratrika", 22,"Kolkata")
obj2.loyalty()