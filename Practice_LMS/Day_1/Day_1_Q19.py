""" Exercise 19 — Count Digits in a Number
 Input: any number (e.g., 3951)
 Output: total digits (4)"""

n=int(input("Enter a number: "))
x=n
c=0
while x>0:
    d=x%10
    c=c+1
    x=x//10
print("Total digits: ",c)