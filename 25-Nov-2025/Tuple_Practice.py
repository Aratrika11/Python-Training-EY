"""Exercise 1
Given a tuple containing both numbers and strings, separate them into two tuples: one containing only
numbers and one containing only strings."""

t=(1,"cat",11,21,"rat")
n=[]
s=[]
for i in t:
    if isinstance(i,(int,float)):
        n.append(i)
    if isinstance(i,str):
        s.append(i)
tn=tuple(n)
ts=tuple(s)
print("Tuple of numbers",tn)
print("Tuple of strings",ts)

"""Exercise 2
Given a tuple of numbers, determine whether it is strictly increasing."""

t=(1,2,3,4,10,5,6,7)
x=t[0]
c=0
for i in t:
    if i>x:
        c=c+1
        x=i
if c==len(t):
    print("Strictly increasing")
else:
    print("Not strictly increasing")

"""Exercise 3

Create a tuple of words and return a new tuple where each word is reversed.
Input: ("python", "cloud", "data")
Output: ("nohtyp", "duolc", "atad")"""

t=("python", "cloud", "data")
l=[]
for i in t:
    s=i[::-1]
    l.append(s)
t=tuple(l)
print("Tuple of reversed words",t)

"""Exercise 4
Write a program to find the index positions of a given value inside a tuple, without using index()"""

t=(40,30,50,20,60,10,70)
print(t)
n=int(input("Enter a number the position of which you want: "))
for i in range(0,len(t)):
    if t[i]==n:
        break
print("Index of ",n," is ",i+1)

"""Exercise 5
Given a tuple (10, (20, 30), (40, (50, 60))) , print all integers using recursion."""

def recursion(t):
    for i in t:
        if isinstance(i,(int,float)):
            print(i)
        elif isinstance(i,tuple):
            recursion(i)

t=(10, (20, 30), (40, (50, 60)))
recursion(t)