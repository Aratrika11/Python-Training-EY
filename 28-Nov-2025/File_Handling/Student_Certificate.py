"""1. Student Certificate Batch Generator

Write a program that reads a list of student names from students.txt and generates a certificate
file for each student automatically."""

"""generate_certificate = lambda student: f"Certificate for {student} - Congratulations! on completing the Python Training"

def write_certificate(student,filename):
    with open(filename,"w") as f:
        f.write(generate_certificate(student))
    print(f"Certificate generated for {student}")

write_certificate("Aratrika","Certificate.txt")"""

def generate_certificate():
    with open("students.txt","r") as f:
        students = f.readlines()

    for line in students:
        name=line.lstrip()
        if not name:
            continue

        #safe_name = name.replace(" ","")
        filename = lambda name:f"Certificate for {name} - Congratulations!"
        certificate_txt = f"""
        This is to certify that
                {name}
        has successfully completed the course
        """

        with open("certificate_txt","w") as cf:
            cf.write(certificate_txt.strip())

        print(f"Certificate generated for {name}")

generate_certificate()