"""Exercise 3 — Interchange First and Last Elements
Input:
['a', 'b', 'c', 'd', 'e']
Output:
['e', 'b', 'c', 'd', 'a']
Swap using indexing."""

x=['a','b','c','d','e']
x[0],x[-1]=x[-1],x[0]
print(x)