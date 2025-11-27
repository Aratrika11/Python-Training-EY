class Teacher:
    def __init__(self,name,mode_of_delivery,duration):
        self.name = name
        self.mode_of_delivery = mode_of_delivery
        self.duration = duration
class Content:
    def __init__(self,name,mode_of_delivery,duration):
        self.name = name
        self.mode_of_delivery = mode_of_delivery
        self.duration = duration
class Online_Trainer(Teacher,Content):
    def __init__(self,name,mode_of_delivery,duration,subject):
        Teacher.__init__(self,name,mode_of_delivery,duration)
        Content.__init__(self,name,mode_of_delivery,duration)
        self.subject = subject

ont = Online_Trainer("Aratrika","Live sessions",3,"Maths")
ont2 = Online_Trainer("Aratrika","PPT","Self Paced","Maths")
print(f"Online Trainer {ont.name} teaches {ont.subject} through {ont.mode_of_delivery} for {ont.duration} hrs")
print(f"Online Trainer {ont2.name} teaches {ont2.subject} through {ont2.mode_of_delivery} in {ont2.duration}")
