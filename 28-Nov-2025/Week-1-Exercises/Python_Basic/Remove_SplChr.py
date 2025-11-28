str=input("Enter a string")
rstr=""
for i in str:
    if i.isalnum():
        rstr+=i
print("String without special characters: ",rstr)