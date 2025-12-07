"""Exercise 20 — Reverse a Number (Logic Basics)"""
n=int(input("Enter a number: "))
x=n
s=0
while x>0:
    d=x%10
    s=s*10+d
    x=x//10
print("Reverse: ",s)
