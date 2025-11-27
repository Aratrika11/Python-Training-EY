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

car = Car("Hyundai","Venue","1197cc",5,2024)
print(f"Details of {car.brand} {car.model} are : Engine : {car.engine} Year : {car.year} and {car.seat} seater")