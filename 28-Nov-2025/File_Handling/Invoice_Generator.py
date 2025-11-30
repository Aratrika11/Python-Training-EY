"""4. Invoice Generator from CSV
 Read a CSV le orders.csv containing columns: item, quantity, price.
 Generate an invoice le that lists all items and the nal total"""

import csv
orders = [
    {"item": "Apple", "quantity": 5, "price": 12.50},
    {"item": "Orange", "quantity": 4, "price": 15.50},
    {"item": "Banana", "quantity": 12, "price": 24.50}
]
with open("invoice.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["item", "quantity", "price"])
    writer.writeheader()
    writer.writerows(orders)
print("Invoice.csv created successfully")

calc_total = lambda quantity , price : quantity * price
total=0
with open("invoice.csv","r") as f:
    reader = csv.DictReader(f)
    with open("invoice.log","w") as g:
        for row in reader:
            item = row["item"]
            quantity = int(row["quantity"])
            price = float(row["price"])
            line_total = calc_total(quantity, price)
            total = total + line_total
            g.write(f"{item} x {quantity} Rs.{line_total}\n")
        g.write("\n")
        g.write(f"SubTotal: Rs{total}\n")
print("Invoice.log created successfully")
