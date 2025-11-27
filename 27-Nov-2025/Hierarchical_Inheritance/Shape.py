class Shape:
    def __init__(self,colour):
        self.colour = colour
class Circle(Shape):
    def __init__(self,colour,radius):
        super().__init__(colour)
        self.radius = radius
    def perimeter(self):
        return self.radius*2*3.14
    def area(self):
        return self.radius * self.radius * 3.14
class Rectangle(Shape):
    def __init__(self,colour,width,height):
        super().__init__(colour)
        self.width = width
        self.height = height
    def perimeter(self):
        return 2*(self.width+self.height)
    def area(self):
        return self.width*self.height
class Triangle(Shape):
    def __init__(self,colour,height,base,hypotenuse):
        super().__init__(colour)
        self.height = height
        self.base = base
        self.hypotenuse = hypotenuse
    def perimeter(self):
        return self.base+self.hypotenuse+self.height
    def area(self):
        return self.base*self.height*0.5
obj1 = Circle("red",5)
print("Perimeter= ",obj1.perimeter())
print("Area = ",obj1.area())

obj2 = Rectangle("green",10,5)
print("Perimeter= ",obj2.perimeter())
print("Area = ",obj2.area())

obj3 = Triangle("Black",3,4,5)
print("Perimeter= ",obj3.perimeter())
print("Area = ",obj3.area())