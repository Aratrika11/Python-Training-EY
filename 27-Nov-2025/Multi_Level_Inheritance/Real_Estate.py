class Property:
    def __init__(self,location,type,landmark):
        self.location = location
        self.type = type
        self.landmark = landmark
class Building(Property):
    def __init__(self,location,floor,type,landmark):
        super().__init__(location,type,landmark)
        self.floor = floor
class Apartment(Building):
    def __init__(self,location,floor,type,status,number,landmark):
        super().__init__(location,floor,type,landmark)
        self.status = status
        self.number = number
flat = Apartment("Salt Lake",15,"Residential","Rented",47,"near Nalban")
print(f"The building is {flat.type} located in {flat.location} refer landmark {flat.landmark},the apartment is on {flat.floor} floor")
print(f"Apartment number {flat.number} is {flat.status}")