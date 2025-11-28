"""Exercise 10
Write a log writer program using append mode that adds entries like:
"2025-01-01 10:30:45 - Application started"
Use the datetime module."""

from datetime import datetime
with open("date.txt","a") as f:
    f.write(f"{datetime.now()} --Application Started\n")

print("Contents of date.txt are: ")
with open("date.txt","r") as f:
    print(f.read())