"""try:
    x=10/0
except ZeroDivisionError:
    print("Cannot divide by zero")"""
#Example 2
"""try:
    num=int(input("Enter a number: "))
    print(10/num)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Cannot divide by zero")"""
#Example 3
"""try:
    f=open("test.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("Closing operation completed")"""
#example 4 Try-Else
"""try:
    value = int("50")
except ValueError:
    print("Invalid Number")
else:
    print("Conversion successful")"""
#example 5 raising an exception
"""def check_age(age):
    if age <18:
        raise ValueError("Age must be 18 or above")
    return "Allowed"
print(check_age(20))
print(check_age(15))  #triggers exception"""
#Custom Exception
"""class LowBalanceError(Exception):
    pass
def withdraw(amount,balance):
    if amount > balance:
        raise LowBalanceError("Insufficient funds")
    return balance - amount"""
