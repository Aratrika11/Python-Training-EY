"""#No duplicate allowed
s={1,1,2,3,4,5,5}
print(s)   #{1, 2, 3, 4, 5}"""

"""#Set Creation
s1={1,2,3,4,5,6}
empty=set()
print(empty)"""

"""#Add elements
s2={1,2,3}
s2.add(4)
print(s2)
s2.update([5,6])
print(s2)"""

"""#Deletion
s1.remove(5)
print(s1)
s1.remove(5)
print(s1)
s1.discard(6)
print(s1)"""

a={1,2,3,4,5,6}
b={5,6,7,8}
print(a|b) #union
print(a&b) #intersection
print(a^b) #symmetric Difference
print(a-b)
print(b-a)

#Uniqueness
l=[1,1,2,2,3,6,7,8,8]
uniquee=list(set(l))
print(uniquee)