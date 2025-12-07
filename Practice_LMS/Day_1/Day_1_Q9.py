"""Exercise 9
Create a class Mobile with attributes brand, model, storage. Add a method to upgrade storage."""

class Mobile:
    def __init__(self,brand,model,storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    def upgrade(self):
        sto=int(input("Enter the new storage after upgradation"))
        self.storage = sto
        print(f"Mobile: {self.brand} - {self.model}, Storage upgraded to: {self.storage} GB")

obj3 = Mobile("Samsung","S25 ultra",12)
obj3.upgrade()