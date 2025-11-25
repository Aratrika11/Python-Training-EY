"""Exercise 1
Given two sets, print the elements that are present in the union but not in the intersection.
(Equivalent to symmetric difference but do not use ^ .)"""

"""s={1,2,3,4,5,6}
s1={5,6,7,8}
a=(s|s1)
b=(s & s1)
print("Element in union but not in intersection: ",a-b)"""

"""Exercise 2
Given a list with duplicates, convert it to a set and then back to a list, preserving the original order of
first occurrences."""

"""l=[20,10,20,30,40,30,50]
r=[]
for i in l:
    if i not in r:
        r.append(i)
print("Original list without duplicates: ",l)
print("New list without duplicates: ",r)"""

"""Exercise 3

Given a set of numbers, find all pairs that sum up to a target number.
Example:
Set = {2, 4, 6, 8, 10}
Target = 12
Output: (2, 10), (4, 8), (6, 6)
Without reusing same pairs twice."""

"""s={2,4,6,8,10}
s1=list(s)
target = int(input("Enter a target number: "))
print("Pairs are")
for i in range(0,len(s1)):
    for j in range(i+1,len(s1)):
        if s1[i]+s1[j]==target:
            print(s1[i],s1[j])
        elif s1[i]+s1[i]==target:
            print(s1[i],s1[i])"""

"""Exercise 4
Check whether two sets are disjoint without using the built-in method."""

"""s={1,2,3,4,5}
s1={6,7,8,9,10}
c=0
for i in range(0,len(s)):
    for j in range(i,len(s1)):
        if i in s1:
            c=c+1
if c==0:
    print("The sets are disjoint")"""

"""Exercise 5
Given a list of words, find all unique characters across all words combined, using sets."""

l=["cat","car","rat","mat"]
unichar=set()
for i in l:
    unichar.update(i)
print(unichar)

