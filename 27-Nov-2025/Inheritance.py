"""class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def barks(self):
        print("Dog barks")
d = Dog()
d.speak()
d.barks()"""

class Person:
    def __init__(self, name):
        self.name = name
class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id
emp=Employee("Aratrika",23456)
print(emp.name)
print(emp.emp_id)