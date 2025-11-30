"""Exercise 8
Write a program to read a CSV file named students.csv and print name and marks of each student."""

import csv
with open("students.csv") as f:
    reading = csv.reader(f)

    for row in reading:
        name = row[0]
        marks = row[1]
        print(f"Name: {name}, Marks: {marks}")