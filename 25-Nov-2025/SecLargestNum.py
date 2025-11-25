"""Exercise 1 — Second Largest Number (Without Sorting)
Given a list:
nums = [23, 89, 12, 78, 55, 42]
Find the second largest number without using sort() or max() ."""

nums=[23,89,12,78,55,42]
x=mx=0
for i in nums:
    if i>x:
        x=i
for j in nums:
    if j>mx and j<x:
        mx=j
print("Second Largest Number is ",mx)

