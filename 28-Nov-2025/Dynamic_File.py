generate_line = lambda user: f"Hello {user} ,welcome too Python Training."
def write_dynamic_line(user,filename):
    with open(filename,"w") as f:
        f.write(generate_line(user))
write_dynamic_line("Aratrika","Welcome.txt")