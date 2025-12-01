""" Write a program that takes two numbers as input and handles division by zero using try–except
try:
    num=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    x=num/num2
    print(x)
except ZeroDivisionError:
    print("Cannot divide by zero")"""
import csv

#Write a program to read a file. Handle FileNotFoundError and PermissionError.
"""try:
    f=open("test.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
finally:
    print("Closing operation")"""

#Write a function that converts a string to integer and handles invalid inputs.
"""try:
    n=input("Enter a value: ")
    val=int(n)
    print(val)
except ValueError:
    print("Invalid Conversion")"""

#Build a safe list access function: if index is out of range, return a message instead of error.
"""def safe_access(l,ind):
    try:
        value=l[ind]
    except IndexError:
        print("Index out of range")
    else:
        print(value)
safe_access([1,2,3],0)
safe_access([1,2,3],4)"""

# Write a program to open a CSV file and handle incorrect file format errors.
"""import csv
file = "data.csv"
try:
    with open(file,"r") as cfl:
        reader = csv.reader(cfl)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")
except csv.Error:
    print("Error: Incorrect CSV file format")"""

#Create a function that raises a custom exception InvalidAgeError if age < 18.
"""def check_age(age):
    if age <18:
        raise ValueError("Age must be 18 or above")
    return "Allowed"
print(check_age(20))
print(check_age(15))"""

#Write a program that attempts to convert items of a list to integers, handling conversion errors individually.
"""l=["a",123,"Aratrika",True,20.5]
for i in l:
    try:
        value=int(i)
        print(value)
    except ValueError:
        print(i,"Invalid Conversion")"""

#Create a bank withdrawal function that raises LowBalanceError when balance is insufficient.
"""class LowBalanceError(Exception):
    pass
def withdraw(amount,balance):
    if amount > balance:
        raise LowBalanceError("Insufficient funds")
    return balance - amount

try:
    print(withdraw(120, 100))
except LowBalanceError as e:
    print("Withdrawal failed:", e)"""

#Write a safe calculator function that handles invalid operators and incorrect inputs.
"""def calc(a,b,op):
    try:
        a= float(a)
        b= float(b)
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Error: Invalid operator"
    except ValueError:
        return "Error: Input must be a number"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
print(calc(10,20,"*"))
print(calc(10,20,"+"))
print(calc(10,0,"/"))
print(calc(10,20,"&"))"""

#Write a program using try–except–else–finally to read user input and write it into a file safely.
file = "test.txt"
try:
    text=input("Enter text to be added into the file: ")
    cfl = open(file,"w")
except Exception as e:
    print("Error opening file: ",e)
else:
    try:
        cfl.write(text+"\n")
        print("Text added into the file")
    except Exception as e:
        print("Error writing file: ",e)
    finally:
        print("File is closed")