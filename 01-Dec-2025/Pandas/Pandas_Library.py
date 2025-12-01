import pandas as pd

#Series
s=pd.Series([1,2,3,4,5,6])
print(s)

#DataFrame
data = {
    "Name": ["Aratrika","Nirakshi","Titli"],
    "Marks": [98,94,90]
}

df = pd.DataFrame(data)
print(df)