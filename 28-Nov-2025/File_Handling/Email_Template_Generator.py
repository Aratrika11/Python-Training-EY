"""11. Email Template Generator
 Write a script that reads names from names.txt and generates email templates like:
Dear <name>,
Your training session starts tomorrow.
Regards,
Training Team
Each email should be saved into separate les"""

with open("students.txt","r") as f:
    names = f.readlines()

for name in names:
    name = name.strip()
    email_text = (
        f"Dear {name},\n"
        "Your Training session is ongoing. You are requested to attend it diligently.\n"
        "Regards,\n"
        "Training Team\n"
    )
filename = f"{name}.txt"
with open(filename,"w") as ef:
    ef.write(email_text)

print("Email generated successfully")