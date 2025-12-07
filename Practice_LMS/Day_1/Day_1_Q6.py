"""Exercise 6
Create a class Product with attributes name, price, quantity. Add a method to calculate the
total cost of all quantities."""

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def totalcost(self):
        cost=self.price*self.quantity
        print(f"Product: {self.name},Quanity: {self.quantity},Total Cost: {cost}")

obj1 = Product("Water Bottle",90,5)

obj1.totalcost()