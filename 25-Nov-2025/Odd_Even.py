"""Exercise 7 — Separate Even and Odd into Two Lists
Input:
nums = [10, 3, 5, 12, 8, 7, 1]
Output:
Even: [10, 12, 8]
Odd: [3, 5, 7, 1]"""

num=[10,3,5,12,8,7,1]
x=[]
y=[]
for i in num:
    if i%2==0:
        x.append(i)
    else:
        y.append(i)
print("Even: ", x)
print("Odd: ", y)