"""24. Read a text file and count: characters, words, lines.
with open("Sampletext.txt","r") as f:
    text = f.read()
print("Characters:",len(text))
print("Words:",len(text.split()))
print("Lines:",len(text.splitlines()))"""
import csv

"""25. Create a CSV file storing 20 employees and read it back into a dictionary list.
employees = [{"id": i,"name": f"Emp{i}"} for i in range(1,21)]
with open("employees.csv","w") as f:
    writer = csv.DictWriter(f,fieldnames=["id","name"])
    writer.writeheader()
    writer.writerows(employees)
with open("employees.csv","r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)"""

"""26. Write a program that appends log entries to a logfile with timestamps.
from datetime import datetime
with open("Introduction.txt","a") as file:
    file.write(f"\n{datetime.now()} --Entry Recorded\n")"""

"""27.Build a program that loads a JSON file of products, adds a discount, and writes back.
import json
products = json.load(open("products.json"))
for p in products:
    p["price"] *= 0.9 #10% discount

json.dump(products,open("products.json","w"), indent=2)"""

"""28. Split a text file into two files: first half and second half.
with open("input.txt","r") as f:
    lines = f.readlines()
mid = len(lines)//2
open("first_half.txt","w").writelines(lines[:mid])
open("second_half.txt","w").writelines(lines[mid:])"""

"""29. Convert a CSV file to JSON using Python.
import csv,json
with open("data.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)
json.dump(data,open("data.json","w"),indent=2)"""