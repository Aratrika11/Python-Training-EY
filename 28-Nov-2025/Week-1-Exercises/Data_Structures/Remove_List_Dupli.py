n=int(input("Enter a number: "))
elements=[]
for i in range(n):
    elements.append(input(f"Enter element {i+1}: "))
print("List: \n",elements)

new_list=[]
for i in elements:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates: ",new_list)
