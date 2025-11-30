"""40. Create a class Score that overloads the + operator to combine two scores, and overloads > to
 compare them"""

class Score:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return Score(self.value + other.value)
    def __gt__(self,other):
        return self.value>other.value
s1=Score(5)
s2=Score(20)

combined = s1 + s2
print("Combined Overloaded +: ",combined)
print("Overloaded >: ")

if s1>s2:
    print(f"{s1.value}>{s2.value}")
else:
    print(f"{s1.value}<{s2.value}")
