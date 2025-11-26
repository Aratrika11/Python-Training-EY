class Shopping:
    def __init__(self):
        self.items=[]
    def add_item(self,name,price):
        self.items.append((name,price))
        print(name,"added to cart")

    def remove_item(self,name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print(name,"removed from cart")
                return
        print(name,"not found in cart")

    def total_cost(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total

    def discount(self,percent):
        total=self.total_cost()
        discount_amt=total * (percent/100)
        final_price = total - discount_amt
        return final_price

    def display_items(self):
        if not self.items:
            print("Cart is empty")
            return
        print("Items in cart:")
        for name, price in self.items:
            print(name,"-",price)

cart=Shopping()

cart.add_item("Laptop",55000)
cart.add_item("Mouse",800)
cart.add_item("Keyboard",1500)

print()
cart.display_items()
print()

print("Total cost:",cart.total_cost())
print("Final Price after 10% discount:",cart.discount(10))
print()
cart.remove_item("Mouse")
cart.display_items()
