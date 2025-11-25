"""Exercise 1
Given a list of integers, rearrange the list so that all negative numbers appear first and all positive
numbers appear later, without using additional predefined functions like sort() ."""

l=[20,45,-10,15,3,-1,-40,]
n=[]
p=[]
for i in l:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
r=n+p
print(r)

"""Exercise 2
Given a list, create a new list that contains only those elements which appear more than once. Do not
use set() ."""

l=[1,2,3,4,2,1,5,1]
c=0
x=[]
for i in l:
    c=0
    for j in range(0,len(l)):
        if i==l[j]:
            c+=1
    if c>1 and i not in x:
        x.append(i)
print("Multi occurence: ",x)

"""Exercise 3
Rotate a list to the left by N positions using only loops."""

l=[10,20,30,40,50]
n=int(input("Enter the number of positions (less than 5 - list length) by which you want to rotate the list "))
n=n%len(l)
r=[]
for i in range(n,len(l)):
    r.append(l[i])
for i in range(n):
    r.append(l[i])
print("Original list:",l)
print("Rotated list:",r)

"""Exercise 4
Given a list of strings, remove all strings whose length is less than 3."""

l=["at","cat","fiat","to","q","tom"]
x=list(l)
for i in x:
    if len(i)<3:
        l.pop(l.index(i))
print("Original list:",x)
print("New list:",l)

"""Exercise 5
Flatten a nested list using loops only.
Example:
Input: [[1, 2], [3, 4], [5]]
Output: [1, 2, 3, 4, 5]"""

l=[[1, 2], [3, 4], [5]]
ll=[]
for i in l:
    for j in i:
        ll.append(j)
print("Original list:",l)
print("Flattened list:",ll)
