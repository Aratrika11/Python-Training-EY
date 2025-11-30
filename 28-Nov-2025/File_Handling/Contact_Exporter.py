with open("contacts.csv","r") as f:
    lines=f.readlines()

with open("contacts_export.txt","w") as file:
    for line in lines[1:]:
        name,phone = line.strip().split(",")
        file.write(f"Name: {name} | Phone: {phone}\n")

print("Contacts Exported Successfully")