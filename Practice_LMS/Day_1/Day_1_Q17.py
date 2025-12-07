"""Exercise 17 — Sum of First N Natural Numbers.
Ask for N. Use a loop to compute the sum."""
sum=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
    sum=sum+i
print(sum)