#writing to a file
with open("Sample.txt","w")as f:
    f.write("Hello World \n")
    f.write("I am at training")

#reading from a file
with open("Sample.txt","r")as f:
    content = f.read()
    print(content)
