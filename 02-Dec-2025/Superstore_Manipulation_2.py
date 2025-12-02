import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("Superstore.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])
"""F. PIVOT TABLES (5)
Create pivot: Rows = Region, Columns = Category, Values = Sales.
Pivot showing Profit by SubCategory and Segment.
Pivot showing count of orders by Returned status and Region.
Pivot showing average UnitPrice per Category.
Pivot showing total Quantity per Month and Region."""
"""pivot_table1 = df.pivot_table(
    values = "Sales",
    index = "Region",
    columns = "Category",
    aggfunc = "sum"
)
print(pivot_table1)
pivot_table2 = df.pivot_table(
    values = "Profit",
    index = "SubCategory",
    columns = "Segment",
    aggfunc = "sum"
)
print(pivot_table2)
pivot_table3 = df.pivot_table(
    values = "OrderID",
    index = "Returned",
    columns = "Region",
    aggfunc = "sum"
)
print(pivot_table3)
pivot_table4 = df.pivot_table(
    values = "UnitPrice",
    index = "Category",
    aggfunc = "mean"
)
print(pivot_table4)
df["Month"]=df["OrderDate"].dt.month
pivot_table5 = df.pivot_table(
    values = "Quantity",
    index = "Month",
    columns = "Region",
    aggfunc = "sum"
)
print(pivot_table5)"""

"""G. JOINING / MERGING (4)
Create a discount lookup: Consumer=5, Corporate=8, Home Office=10 and merge it.
Create a region tax table and merge.
Merge customer-level totals into the main df.
Merge product-level profitability summary."""

"""disc_lookup = pd.DataFrame({
    "Segment": ["Consumer","Corporate","Home Office"],
    "SegmentDiscount": [5,8,10]
})
df=df.merge(disc_lookup,on="Segment",how="left")
print(df)
#33
region_tax = pd.DataFrame({
    "Region": ["West","East","Central","South"],
    "TaxRate": [0.08,0.06,0.07,0.05]
})
df = df.merge(region_tax,on="Region",how="left")
print(df)
#34
customer_totals = df.groupby("CustomerName")[["Sales","Profit"]].sum().reset_index()
customer_totals.rename(columns={"Sales":"TotalSales","Profit":"TotalProfit"},inplace=True)
df =df.merge(customer_totals,on="CustomerName",how="left")
print(df)
#35
prod_profit = df.groupby("ProductName")["Profit"].sum().reset_index()
prod_profit.rename(columns = {"Profit":"Total_Product_Profit"}, inplace = True)
df =df.merge(prod_profit,on="ProductName",how="left")
print(df)"""

"""H. DATE OPERATIONS (5)
Extract year, month, day from OrderDate.
Calculate which day of week each order was placed.
Find orders shipped in more than 5 days.
Group orders by month and compute sales.
Plot sales trend per month (line chart)."""
#36
df["OrderYear"] = df["OrderDate"].dt.year
df["OrderMonth"]= df["OrderDate"].dt.month
df["OrderDay"]=df["OrderDate"].dt.day
print(df)
#37
df["OrderWeek"] = df["OrderDate"].dt.day_name()
print(df)
#38
df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
shipped_5days = df[df["ShippingDays"]>5]
print(shipped_5days)
#39
sales_per_month = df.groupby("OrderMonth")["Sales"].sum()
print(sales_per_month)
#40
plt.figure(figsize = (10,6))
#sales_per_month.plot(kind = "line")
plt.plot(sales_per_month,marker="o",linestyle="-",label="Total Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Sales Trend per Month")
plt.grid(True)
plt.show()