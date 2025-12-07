"""Exercise 14 — Swap Two Variables
Ask for two numbers. Swap them without using a third variable"""

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
a=a+b
b=a-b
a=a-b
print(f"After swapping a = {a} and b = {b}")