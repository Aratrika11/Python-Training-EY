n=int(input("Enter a number: "))
elements=[]
for i in range(n):
    elements.append(input(f"Enter element {i+1}: "))
print("List: \n",elements)

l=[]
for i in elements:
    if len(i)>4:
        l.append(i)
print("List of strings with length above 4\n")
print(l)