import pandas as pd
"""A. DATA LOADING & INSPECTION (5)
1. Load the CSV and display first 10 rows.
2. Show total number of rows and columns.
3. Find data types of each column.
4. Identify columns containing missing values.
5. Convert OrderDate and ShipDate to datetime."""
df =pd.read_csv("Superstore.csv")
print("First 10 rows\n")
print(df.head(10))
print("Total number of rows and columns\n")
print(df.shape)
print("Data types of each column\n")
print(df.dtypes)
print("Columns with missing values\n")
print(df.isnull().sum())
print("After converting Orderdate and Shipdate to datetime\n")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])
print(df)

"""B. CLEANING & TRANSFORMATIONS (5)
6. Create a new column ShippingDays = ShipDate - OrderDate.
7. Create ProfitMargin = Profit / Sales.
8. Standardize CustomerName to title case.
9. Remove rows where Sales is zero or negative.
10. Convert Discount from decimal to percentage format."""

df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
df["ProfitMargin"]=df["Profit"]/df["Sales"]
df["CustomerName"]= df["CustomerName"].str.title()
df = df[df["Sales"]>0]
df["Discount"] = df["Discount"]*100
print(df)

"""C. FILTERING (5)
11. Filter all orders from the West region.
12. Filter Technology category with Sales > 400.
13. Find all products returned by customers.
14. Show Furniture orders shipped after 2024-01-20.
15. Filter orders where Profit < 20.

west_orders = df[df["Region"]=="West"]
print("West Region\n")
print(west_orders)
tech_sales = df[(df["Sales"]>400) & (df["Category"]=="Technology")]
print("Technology category\n")
print(tech_sales)
product_returned = df[df["Returned"] == "Yes"]
print("Products Returned\n")
print(product_returned)
furniture = df[(df["Category"]=="Furniture")&(df["ShipDate"]>"2024-01-20")]
print("Furniture ordered after 2024-01-20\n")
print(furniture)
orders = df[(df["Profit"]< 20)]
print("Orders with profit below 20\n")
print(orders)"""

"""D. SORTING (5)
16. Sort by Sales descending.
17. Sort by ProfitMargin.
18. Sort by Region then City.
19. Sort by ShippingDays largest to smallest.
20. Sort by CustomerName alphabetical."""

df_desc_sort = df.sort_values("Sales",ascending=False)
#print("Sales Descending sort\n")
#print(df_desc_sort)
df_profitmargin = df.sort_values("ProfitMargin",ascending=False)
#print("ProfitMargin sort\n")
#print(df_profitmargin)
df_sort_Region_City = df.sort_values(["Region","City"],ascending=False)
#print("Sort by region then by city\n")
#print(df_sort_Region_City)
df_shippingdays_sort = df.sort_values("ShippingDays",ascending=False)
#print("ShippingDays sort\n")
#print(df_shippingdays_sort)
df_customer_sort = df.sort_values("CustomerName",ascending=False)
#print("Sort by customers\n")
#print(df_customer_sort)

"""E. GROUPBY ANALYSIS (6)
21. Total Sales per Region.
22. Average Profit per Category.
23. Count of orders per Customer.
24. Sum of Sales per Segment.
25. Total Quantity sold per SubCategory.
26. Mean ShippingDays grouped by Category."""

tot_sale_region = df.groupby("Region")["Sales"].sum()
print("Total sales per region\n")
print(tot_sale_region)
avg_profit_category = df.groupby("Category")["Profit"].mean()
print("Average profit per category\n")
print(avg_profit_category)
order_count_customer = df.groupby("CustomerName")["OrderID"].count()
print("Count of orders per customer\n")
print(order_count_customer)
sales_sum_segemnt = df.groupby("Segment")["Sales"].sum()
print("Sum of sales per segment\n")
print(sales_sum_segemnt)
tot_quantity_SubCat = df.groupby("SubCategory")["Quantity"].sum()
print("Total quantity per subcategory\n")
print(tot_quantity_SubCat)
mean_shipping_category = df.groupby("Category")["ShippingDays"].mean()
print("Mean shipping days per category\n")
print(mean_shipping_category)
