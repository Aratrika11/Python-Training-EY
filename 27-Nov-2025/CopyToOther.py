with open("Notes.txt","r") as f:
    content = f.readlines()
    with open("Note.txt","w") as ff:
        for i in content:
            ff.write(i)
