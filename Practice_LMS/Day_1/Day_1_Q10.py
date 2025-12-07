"""Exercise 10
Create a class Student with three subject marks. Add methods for total, percentage, and grade
(A, B, C, D)."""

class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total(self):
        return self.m1 + self.m2 + self.m3

    def percent(self):
        return (self.total() / 300) * 100

    def grade(self):
        if self.percent()>=90:
            return "A"
        elif self.percent()<90 and self.percent()>=75:
            return "B"
        elif self.percent()<75 and self.percent()>=60:
            return "C"
        else:
            return "D"

    def display(self):
        print("Name:", self.name)
        print("MARKS: ", self.m1, self.m2, self.m3)
        print("TOTAL:", self.total())
        print("PERCENTAGE:", self.percent())
        print("GRADE:", self.grade())


s1 = Student("Aratrika", 96, 95, 90)
s1.display()