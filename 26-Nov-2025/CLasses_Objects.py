"""class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("Aratrika",22)
s2=Student("Titli",24)
print(s1.name)
print(s2.name)"""

"""class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print("Brand",self.brand)
        print("Model",self.model)
        print("Price",self.price)
#Creating object
car1=Car("Toyota","Fortuner",4500000)
car2=Car("Maruti","WagonR",200000)

#Displaying by calling method
car1.display()
print() #to send to nextline
car2.display()"""

class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary

    def display(self):
        print("Employee ID",self.emp_id)
        print("Name",self.name)
        print("Department",self.department)
        print("Salary",self.salary)

e1 = Employee(101,"Aratrika","IT",95000)
e2 = Employee(102,"Nirakshi","Finance",85000)

e1.display()
print()
e2.display()
