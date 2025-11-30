"""Exercise 5
Write a program that reads a file and counts the number of words in it."""
c=0
with open("Notes.txt","r") as f:
    content=f.read()
    words=content.split()
    print("Total number of words: ",len(words))
