class Calculator:
    def __init__(self):
        pass
    def addition(self,n1,n2):
        print("Sum: ",(n1+n2))
    def subtraction(self,n1,n2):
        print("Subtraction: ",(n1-n2))
    def multiplication(self,n1,n2):
        print("Multiplication: ",(n1*n2))
    def division(self,n1,n2):
        if n1==0:
            print(f"{n2} / {n1} not possible")
        elif n2==0:
            print(f"{n1} / {n2} not possible")
        else:
            print(f"Division of {n1} by {n2}: ",(n1/n2))
obj1 = Calculator()
obj2 = Calculator()

obj1.addition(10,20)
obj1.subtraction(40,20)
obj1.multiplication(5,20)
obj1.division(10,20)
obj2.division(0,20)

