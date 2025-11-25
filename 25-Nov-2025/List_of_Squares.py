"""Exercise 6— Create a New List of Squares (Without Comprehension)
Input:
[2, 4, 6, 8]
Output:
[4, 16, 36, 64]"""

num=[2,4,6,8]
for i in range(0,len(num)):
    num[i]=num[i]**2
print("List of Squares: ",num)