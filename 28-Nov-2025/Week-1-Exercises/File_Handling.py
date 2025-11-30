"""21. . Write a program to create a le and write 5 lines into it.

with open("Introduction.txt","w") as file:
    file.write("Hello !!\n")
    file.write("I am Aratrika Debnath\n")
    file.write("I am currently working in EY GDS\n")
    file.write("Where I am doing a training on Python.\n")
    file.write("Bye!!")"""

"""22. Write a program to read a le and count the number of lines containing the word "Python".

with open("Introduction.txt","r") as file:
    lines = file.readlines()
c=0
for line in lines:
    if "Python" in line:
        c+=1
print(f"{c} line contain Python")"""

"""23. . Write a program to append a timestamped log entry into a file.

from datetime import datetime
with open("Introduction.txt","a") as file:
    file.write(f"\n{datetime.now()} --Entry Recorded\n")"""

"""24. Read a CSV le and print only rows where marks > 75.

import csv

with open("students.csv","w") as file:
    file.write("Student Name,Marks\n")
    file.write("Aratrika Debnath,90\n")
    file.write("Titli Ghosh,74\n")
    file.write("Nirakshi Kundu,80\n")

with open("students.csv","r") as f:
    reading = f.readlines()

    for r in reading[1:]:
        name,marks = r.strip().split(",")
        if int(marks) > 75:
            print(f"Name: {name}, Marks: {marks}")"""
            
"""25.  Create a file that stores the squares of numbers from 1 to 20.

with open("squares_of_numbers.txt", "w") as f:
    for i in range(1, 21):
        f.write(f"{i}^{i} = {i**2}\n")"""
