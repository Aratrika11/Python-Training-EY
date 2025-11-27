class Animal:
    def __init__(self,name):
        self.name = name
class Mammal(Animal):
    def __init__(self,name,habitat):
        super().__init__(name)
        self.habitat = habitat
class Dog(Mammal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.habitat = habitat
        self.breed = breed
dog = Dog("Dog","Land","Australian Shepherd")
print(f"The  animal is {dog.name} that lives on {dog.habitat} and is of the breed {dog.breed}")