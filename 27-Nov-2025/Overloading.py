"""class Mathops:
    def add(self,a,b=0,c=0):
        return a + b + c
n= Mathops()
print(n.add(1,2))
print(n.add(2))
print(n.add(3,4))"""

class Mathops:
    def add(self,*args):
        return sum(args)
n= Mathops()
print(n.add(1,2))
print(n.add(2,3))