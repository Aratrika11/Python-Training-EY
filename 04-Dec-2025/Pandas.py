import pandas as pd
""" 30. Load a 100-row retail dataset and nd: total orders, total revenue, and top 5 products.
df = pd.read_csv("retail.csv")
total_orders = len(df)
total_revenue = df["price"].sum()
top_5prods = df["product"].value_counts().head(5)

print(total_orders,total_revenue,top_5prods)"""

"""31. Identify missing values and fill numeric columns with median, categorical with mode.
df = pd.read_csv("data.csv")
num_cols = df.select_dtypes(include="number").columns
df[num_cols] =df[num_cols].fillna(df[num_cols].median())

category_columns = df.select_dtypes(include="category").columns
df[category_columns]=df[category_columns].fillna(df[category_columns].mode().iloc[0])"""

"""32. Group by product category and calculate: total sales, count of orders, average price.
grouped = df.groupby("category").agg(total_sales = ("price","sum"),
                                     count_orders = ("product","count"),
                                     average_price = ("price","mean"))
print(grouped)"""

"""33. Create a new column "DiscountedPrice" = price minus 10 percent.
df["DiscountedPrice"]= df["price"]*0.9"""

"""34.Merge a customers.csv and orders.csv on customer_id and generate a combined report.
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
merged = customers.merge(orders, on="customer_id")
print(merged.head())"""

"""35. Load a JSON le containing customers and normalize nested fields.
import json
data = json.load(open("customers.json"))
df = pd.json_normalize(data)
print(df.head())

36.*Filter transactions for customers who spent more than 5000 total.
customer_totals = df.groupby("customer_id")["price"].sum()
high_spenders = customer_totals[customer_totals>5000].index

filtered = df[df["customer_id"].isin(high_spenders)]
print(filtered)"""

"""*37. Generate pivot table: category vs month showing total sales.
df["month"] = pd.to_datetime(df["date"]).dt.month

pivot = df.pivot_table(values = "price",index = "category", columns = "month", aggfunc = "sum")
print(pivot)"""

"""*38. Remove outliers using IQR and list the cleaned dataset.
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1
cleaned = df[(df["price"]>=Q1 - 1.5*IQR) & (df["price"]<= Q3 + 1.5*IQR)]
print(cleaned)"""

"""*39. Combine multiple CSVs into one nal DataFrame and remove duplicates
import glob
files = glob.glob("data/*.csv")

df_list = [pd.read_csv(f) for f in files]
final_df = pd.concat(df_list, ignore_index=True).drop_duplicates()

print(final_df)"""