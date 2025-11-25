"""Exercise 2 — Move All Zeros to the End
Input:
[0, 3, 0, 5, 7, 0, 9]
Output:
[3, 5, 7, 9, 0, 0, 0]
Do not use sort() ."""""

l=[0,3,0,5,7,0,9]
r=[]
n=[]
m=[]
for i in range(0,len(l)):
    if l[i]!=0:
        n.append(l[i])
    elif l[i]==0:
        m.append(l[i])
r=n+m
print(r)


