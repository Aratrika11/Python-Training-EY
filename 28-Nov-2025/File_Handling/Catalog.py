""" 7. Product Catalog Formatter
 Read a text le products.txt with product names and prices.
 Generate a formatted catalog le catalog.txt with alignment.
 Example format:
 Product       Price
Laptop        55000
Mouse         800 """

products = [
    "laptop,50000",
    "keyboard,2000",
    "mouse,1000",
    "monitor,20000",
    "printer,10000"
]
with open("products.txt","w") as f:
    for p in products:
        f.write(f"{p}\n")
format_line = lambda p,price : f"{p:<15} {price:>5} \n"
with open("products.txt") as f:
    lines = [line.strip() for line in f]

with open("catalog.txt","w") as cg:
    cg.write("Products      Price\n")
    cg.write("\n")
    for l in lines:
        parts = l.split(",")
        if len(parts) != 2:
            continue
        item,price= parts
        item=item.strip()
        price=price.strip()
        cg.write(f"{format_line(item,price)}")
print("Catalog Created")