c=0
with open("Notes.txt","r") as f:
    #content = f.read()
    for i in f:
        c=c+1
    print(c)

#OR
with open("Notes.txt","r") as f:
    lines = f.readlines()
    print("Number of Lines: ",len(lines))