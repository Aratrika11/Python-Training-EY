
str=input("Enter a string: ")
characters = []
count = []
str=str.lower()
for char in str:
    if char in characters:
        index=characters.index(char)
        count[index] +=1
    else:
        characters.append(char)
        count.append(1)
for i in range(0,len(characters)):
    print(f"{characters[i]} is {count[i]} times")
