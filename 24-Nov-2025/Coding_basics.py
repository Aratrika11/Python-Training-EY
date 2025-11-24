#Exercises on Variable assignment , Loops and If - Else concept

'''Exercise 1 — Simple Calculator
Write a Python program that:
Asks the user for two numbers. Prints the sum, difference, product, and division'''

"""a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print("Sum:",a+b)
print("Difference=",a-b)
print("Product:",a*b)
print("Division:",a/b)"""

"""Exercise 2 — Age in 2050
Write a program that:
Accepts the user’s birth year. Calculates their age in the year 2050"""

'''y=int(input("Enter birth year: "))
print("Age in 2050:",(2050-y))'''

"""Exercise 3 — Area of a Rectangle
 Write a program to calculate: Area = length × width"""

"""l=int(input("Enter length of Rectangle:"))
b=int(input("Enter breadth of rectangle:"))
print("Area =",l*b)"""

"""Exercise 4 — Even or Odd
 Write a Python program that
 Accepts a number. Prints whether it is even or odd"""

"""n=int(input("Enter a number: "))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")"""

"""Exercise 5 — Simple Login Check
 Write a program that asks:
 username
 password
 If both match admin / 1234, print Login Successful, else print Invalid Login."""

'''use=input("Enter Username:")
password=int(input("Enter password:"))
if(use=="admin" and password==1234):
    print("Login Successful")
else:
    print("Invalid")'''


'''Exercise 12 — Square & Cube of a Number
Ask the user for a number. Print its square and cube.

n=int(input("Enter a number: "))
print("Square: ",n*n)
print("Cube:",n**3)'''

 
'''Exercise 13 — Convert Minutes to Hours & Minutes
Take total minutes as input. Convert to hours + remaining minutes.

minute=int(input("Enter time in minutes:"))
hr=int(minute/60)
m=minute%60
print(hr,"hrs and ",m,"minutes")'''

 
''' Exercise 14 — Swap Two Variables
Ask for two numbers. Swap them without using a third variable

a=int(input("enter a number"))
b=int(input("Enter another number"))
a=a+b
b=a-b
a=a-b
print("AfterSwapped a=",a,"and b=",b)'''

 
'''Exercise 15 — Check Positive, Negative, or Zero
User enters a number. Print: Positive Negative Zero

a=int(input("Enter a number"))
if(a==0):
    print("zero")
elif(a>0):
    print("Positive")
else:
    print("Negative")'''


'''Exercise 16 — Find the Last Digit of a Number
Ask the user for any number. Print the last digit.

n=int(input("Enter a double digit or more number"))
print("Last digit=",n%10)'''

 
'''Exercise 17 — Sum of First N Natural Numbers
Ask for N. Use a loop to compute the sum
 
n=int(input("Enter how many natural numbers sum you want: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum of", n,"Natural numbers: ",sum)'''

 
'''Exercise 18 — Multiplication Table
Ask the user for a number and print a 1–10 multiplication table.

n=int(input("Enter whose multiplication table you want: "))
for i in range(1,11):
    print(n,"*",i,"= ",n*i)'''


''' Exercise 19 — Count Digits in a Number
Input: any number (e.g., 3951)
Output: total digits (4)

n=int(input("Enter a number greater than 9: "))
c=n
s=0
while(c!=0):
    d=c%10
    s=s+1
    c=n//10
print("Number of digits =",s)'''

 
'''Exercise 20 — Reverse a Number (Logic Basics)
Input: 54321 Output: 12345

n=int(input("Enter a number"))
c=n
s=0
while(c!=0):
    d=c%10
    s=s*10+d
    c=c//10
print("Reverse:",s)'''


#Break and Continue
#Break Statement
"""for i in range(0,20):
 	if i%8==0:
 	    break
 	print(i)"""
#Output: 1 2 3 4 5 6 7

#Continue Statement
"""for i in range(0,20):
 	if i%8==0:
 	    continue
 	print(i)"""
#Output: 1 2 3 4 5 6 7 9 10 11 12 13 14 15 17 18 19 20


#LIST(mutable)
"""fruits=["apple","banana","orange"]
numbers=[1,2,3,4,5]
mixed=["Aratrika",22,4.8]

print(fruits[0])  Output: apple
print(numbers[3])   Output: 4
print(mixed[-1])   Output: 4.8

#Append and Insert Function
fruits.append("mango")
print(fruits)  Output: ["apple","banana","orange","mango"]

fruits.insert(2,"kiwi")
print(fruits)  Output: ["apple","banana","kiwi","orange","mango"]

#Remove and Deletion Function
fruits.remove("kiwi")
print(fruits)   Output: ["apple","banana","orange","mango"]

fruits.pop(2)
print(fruits)   Output: ["apple","banana","mango"]

fruits.pop()
print(fruits)   Output: ["apple","banana"]

del.fruits[0]

print(fruits)   Output: ["banana"]"""
