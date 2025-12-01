import pandas as pd
"""data = {
    "Name": ["Aratrika","Nirakshi","Titli"],
    "Marks": [98,94,90],
    "City" : ["Kolkata","Bangalore","Hyderabad"]
}
df = pd.DataFrame(data)
df.to_csv("student.csv", index=False)
print("CSV file created\n") """
dr = pd.read_csv("student.csv")
print("CSV file successfulyl read\n")
print(dr)