make_letter = lambda name,course:(
    f"Welcome {name}!\n"
    f"We are excited to have you in the {course} course!\n"
    f"Wishing you all the best!!\n"
)
def create_welcome_letter(name,course):
    filename = f"Welcome {name}.txt"
    with open(filename,"w") as file:
        file.write(make_letter(name,course))
people = ["Aratrika","Titli","Nirakshi"]
courses= ["Data Science", "Machine Learning", "Web Development"]
for name,courses in zip(people,courses):
    create_welcome_letter(name,courses)
print("Welcome Letter created")
