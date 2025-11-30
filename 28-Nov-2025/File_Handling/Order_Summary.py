"""9. Order Summary From User Input
 Ask the user for item name, quantity, and price for 3 items.
 Then generate a summary le order_summary.txt with totals"""

items=[]
for i in range(3):
    name = input("Please enter item name: ")
    qty = int(input("Please enter the quantity: "))
    price = float(input("Please enter the price: "))
    items.append((name,qty,price))

total=0
with open("Order_Summary.txt","w") as f:
    for n,q,p in items:
        cost = q*p
        total += cost
        f.write(f"{n} - Quantity:{q}, Price:{p}, Cost: {cost}\n")
    f.write(f"\nTotal Amount: {total}\n")
