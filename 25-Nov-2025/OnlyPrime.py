"""Exercise 4— Extract Only Prime Numbers
Given:
nums = [10, 11, 12, 13, 17, 20, 23]
Output:
[11, 13, 17, 23]"""

nums=[10,11,12,13,17,20,23]
prime=[]
for i in nums:
    if i>1:
        for j in range(2,i//2+1):
            if i % j == 0:
                break
        else:
            prime.append(i)
print(prime)