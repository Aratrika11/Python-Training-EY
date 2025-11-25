numbers=(33,20,30,60,50)
x=0
for i in numbers:
    if i>x:
        x=i
y=numbers[0]
for j in numbers[1:]:
    if j<y:
        y=j
print("MAX= ",x)
print("MIN= ",y)
