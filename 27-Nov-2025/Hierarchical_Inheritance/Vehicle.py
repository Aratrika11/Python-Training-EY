class Vehicle:
    def __init__(self,engine,type,year):
        self.engine = engine
        self.type = type
        self.year = year
class Car(Vehicle):
    def __init__(self,brand,model,engine,seat,year):
        super().__init__(engine,"4 wheeler",year)
        self.brand = brand
        self.model = model
        self.seat = seat
class Bike(Vehicle):
    def __init__(self,brand,model,engine,year):
        super().__init__(engine,"2 wheeler",year)
        self.brand = brand
        self.model = model

car = Car("Hyundai","Venue","1197cc",5,2024)
print(f"Details of {car.type} {car.brand} {car.model} are : Engine : {car.engine} Year : {car.year} and {car.seat} seater")
bk = Bike("Royal Enfield","Super Meteor","650cc",2023)
print(f"Details of {bk.type} {bk.brand} {bk.model} are : Engine : {bk.engine} Year : {bk.year}")