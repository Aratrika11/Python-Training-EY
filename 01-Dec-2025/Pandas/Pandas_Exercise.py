import pandas as pd
import csv
df = pd.read_csv("retail_sales.csv")
#print(df)
"""Pandas Exercises
1. Load the dataset and display:
first 5 rows ,last 5 rows,column names,shape
print("The first 5 rows are:")
print(df.head(5))
print("The last 5 rows are:")
print(df.tail(5))
print("The column names are:")
print(df.columns)
print("The Dataframe summary")
print(df.shape)"""

"""2.Convert the Date column to datetime and extract:
Year Month Day
Add them as new columns.

df["Date"] = pd.to_datetime(df["Date"])
df["Year"]= df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day
print(df)"""
"""3. Calculate total sales (sum of TotalPrice) for each:
Store City Category

#For Store
total_sales_store = df.groupby("Store")["TotalPrice"].sum()
print(total_sales_store)
#For City
total_sales_city = df.groupby("City")["TotalPrice"].sum()
print(total_sales_city)
#For Category
total_sales_category = df.groupby("Category")["TotalPrice"].sum()
print(total_sales_category)"""

"""4. Find the top 5 highest-value orders by TotalPrice.

top_ordr = df.nlargest(5, "TotalPrice")
print("Top 5 highest-value orders are:")
print(top_ordr)"""

"""5. Filter the dataset to show only Electronics products with Quantity > 1.

e_filtered = df[(df["Category"] == "Electronics") & (df["Quantity"] > 1)]
print(e_filtered)"""

"""6. Add a new column Discount:
10 percent discount for Returning customers
5 percent discount for New customers
Compute final price after discount.

df["Discount"]=df["CustomerType"].map({
    "Returning" : 0.10,
    "New" : 0.05
})
df["FinalPrice"]= df["TotalPrice"] * (1- df["Discount"])
print(df)"""

"""7. Find how many orders were paid using:
Cash Credit Card UPI

payment_counts_cash = df[(df["PaymentMethod"]== "Cash")].value_counts()
print("Cash payment\n",payment_counts_cash)
payment_counts_card = df[(df["PaymentMethod"]== "Credit Card")].value_counts()
print("Cash payment\n",payment_counts_card)
payment_counts_upi = df[(df["PaymentMethod"]== "UPI")].value_counts()
print("Cash payment\n",payment_counts_upi)"""

"""8. Group by Category and compute:
Total quantity sold
Total revenue

category_summary = df.groupby("Category").agg(TotalQuantity=("Quantity", "sum"),TotalRevenue=("TotalPrice", "sum"))
print(category_summary)"""

"""9. Identify the store with the highest total sales.

str_total = df.groupby("Store")["TotalPrice"].sum()
highest = str_total.idxmax()
print(highest)"""

"""10. Filter rows where Product name contains the letter “a” or “A”.

filtered_products = df[df["Product"].str.contains("a",case =False, na=False)]
print(filtered_products)"""

"""11. Sort the dataset by Date and then by TotalPrice.

ted_df = df.sort_values(by = ["Date", "TotalPrice"], ascending =False)
print(ted_df)"""

"""12. Find the average revenue per order for each CustomerType.

avg_revnue = df.groupby("CustomerType")["TotalPrice"].mean()
print(avg_revnue)"""
"""13. Create a pivot table:
Rows: Category
Columns: PaymentMethod
Values: TotalPrice (sum)

pivot_table = df.pivot_table(
    values = "TotalPrice",
    index = "Category",
    columns = "PaymentMethod",
    aggfunc = "sum",
    fill_value = 0
)
print(pivot_table)"""

"""14. Write the filtered Electronics-only dataset into a new CSV file.

e_filtered = df[(df["Category"] == "Electronics") & (df["Quantity"] > 1)]
e_filtered.to_csv("Only_Electronics.csv", index = False)"""

"""15. Use method chaining to:
remove rows with Quantity < 2
filter Category = Apparel
compute TotalValue = Quantity * UnitPrice
sort TotalValue descending
reset index
Return the final DataFrame."""

df= (df[df["Quantity"] >=2].query("Category == 'Apparel'").assign(TotalValue = lambda x: x["Quantity"] * x["UnitPrice"])
.sort_values("TotalValue", ascending = False).reset_index(drop = True))
print(df)