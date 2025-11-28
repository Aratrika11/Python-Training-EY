n=int(input("Enter a number: "))
l=[]
for i in range(n):
    l.append(input(f"Enter element {i+1}: "))
print("List: \n",l)

#l=[10,20,30,40,50]
n=int(input("Enter the number of positions (less than list length) by which you want to rotate the list "))
#n=n%len(l)
r=[]
for i in range(n,len(l)):
    r.append(l[i])
for i in range(n):
    r.append(l[i])
print("Original list:",l)
print("Rotated list:",r)