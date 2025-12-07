"""Exercise 15 — Check Positive, Negative, or Zero"""
n=int(input("Enter a number: "))
if n>0:
    print(f"The number {n} is positive.")
elif n<0:
    print(f"The number {n} is negative.")
elif n==0:
    print("The number is zero.")