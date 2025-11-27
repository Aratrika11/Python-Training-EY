class Father:
    def __init__(self):
        pass
    def display(self):
        print("Name: Sourav")
        print("Nationality: Indian")
        print("Mother-Tongue: Bengali")
class Mother:
    def __init__(self):
        pass
    def display1(self):
        print("Name: Piyali")
        print("Nationality: Indian")
        print("Mother-Tongue: Bengali")
class Child(Mother,Father):
    def __init__(self,name,nationality,mother_tongue):
        self.name = name
        self.nationality = nationality
        self.mother_tongue = mother_tongue
chld = Child("Aratrika","Indian","Bengali")
chld.display()
chld.display1()

