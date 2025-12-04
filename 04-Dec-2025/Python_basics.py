"""1. Write a program that reads a string and prints the number of vowels, consonants, and digits.

str = input("Enter a sentence")
c=v=n=0
for i in str:
    for j in i:
        if j in "AEIOUaeiou":
            v=v+1
        elif j.isdigit():
            n=n+1
        elif j.isalpha() and j not in "AEIOUaeiou":
            c=c+1
print("No. of Vowels : ",v)
print("No. of Digits : ",n)
print("No. of Consonants : ",c)"""

"""2. Create a function that takes a sentence and returns a dictionary of word frequencies.

def word_frequency(str):
    str=str.lower()
    for punctuation in ",.!?;:":
        str=str.replace(punctuation,"")
    words=str.split()
    frequency={}
    for word in words:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    for key,value in frequency.items():
        print(key,":",value)
str = input("Enter a sentence")
print(f"Word Frequency in the sentence {str} \n")
word_frequency(str)"""

"""3. Implement a mini calculator with add, subtract, multiply, and divide using functions.

def addition(n1,n2):
    print("Sum: ",(n1+n2))
def subtraction(n1,n2):
    print("Subtraction: ",(n1-n2))
def multiplication(n1,n2):
    print("Multiplication: ",(n1*n2))
def division(n1,n2):
    if n1==0:
        print(f"{n2} / {n1} not possible")
    elif n2==0:
        print(f"{n1} / {n2} not possible")
    else:
        print(f"Division of {n1} by {n2}: ",(n1/n2))

n=int(input("Enter 1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division \n"))
if n==1:
    n1=int(input("Enter number to be added: "))
    n2=int(input("Enter another number to be added: "))
    addition(n1,n2)
elif n==2:
    n1=int(input("Enter number to be subtracted: "))
    n2=int(input("Enter another number to be subtracted: "))
    subtraction(n1,n2)
elif n==3:
    n1=int(input("Enter number to be multiplied: "))
    n2=int(input("Enter another number to be multiplied: "))
    multiplication(n1,n2)
elif n==4:
    n1=int(input("Enter number to be divided: "))
    n2=int(input("Enter another number to be divided: "))
    division(n1,n2)
else:
    print("Invalid Input")"""

"""4. Write a program that reads N numbers and returns the second highest value without sorting.

n=int(input("Enter size of list: "))
nums = []
for i in range(1,n+1):
    r=int(input("Enter number: "))
    nums.append(r)
x=mx=0
for i in nums:
    if i>x:
        x=i
for j in nums:
    if j>mx and j<x:
        mx=j
print("Second Largest Number is ",mx)"""

"""5. Read 10 values and store them into a list without using loops (use list comprehension).

values = [input("Enter a number") for _ in range(10)]
print("The list is \n",values)"""


