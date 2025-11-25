student={"name":"Aratrika",
         "age":22}
print(student)
print(student.get("name"))
student["city"]="Kolkata"
print(student)
student["name"]="Aratrika Debnath"
print(student)
#Deletion
student.pop("city")
print(student)
#student.clear()
#print(student)

#Displaying only the keys or values
for i in student.keys():
    print(i)
for v in student.values():
    print(v)
for k,v in student.items():
    print(k,v)