"""Exercise 7
Write a program that reads a text file and prints only those lines that contain the word "Python" ."""

with open("Notes.txt","a") as ff:
    ff.write("\n I am learning Python")

with open("Notes.txt","r") as f:
    content = f.readlines()
    for i in content:
        if "Python" in i:
            print(i.strip("\n"))