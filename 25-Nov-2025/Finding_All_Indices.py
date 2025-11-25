Exercise 5 — Find All Indices of a Given Value
List:
nums = [5, 2, 7, 5, 9, 5, 3]
If user enters 5 , output:
[0, 3, 5]

nums=[5,2,7,5,9,5,3]
print(nums)
x=[]
n=int(input("Enter the value you want to know the indices for "))
for i in range(0,len(nums)):
    if nums[i]==n:
        x.append(i)
print("Indices of",n,"are",x)