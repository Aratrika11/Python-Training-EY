import pandas as pd
df = pd.read_csv("retail.csv")
"""print(df.head(5))

df["Date"]=pd.to_datetime(df["Date"])
print(df.info())

df["Year"]= df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day
print(df)"""

#Electronics above 10000
"""e_filtered = df[(df["Category"] == "Electronics") & (df["TotalPrice"] > 10000)]
print(e_filtered)
sorted_df = df.sort_values("TotalPrice", ascending=False)
print(sorted_df)
city_orders = df.groupby("City")["OrderID"].count()
print(city_orders)
category_sales = df.groupby("Category")["TotalPrice"].sum()
print(category_sales)"""

#Joining 2 dataframes
customers = pd.DataFrame({
    "CustomerType": ["New","Returning"],
    "Discount":[5,10]
})

merged = df.merge(customers, on="CustomerType" , how = "left")
print(merged)
