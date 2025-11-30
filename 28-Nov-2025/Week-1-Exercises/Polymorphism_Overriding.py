"""38.  Create two classes Cat and Dog. Both should have a method sound() that behaves differently
class Cat():
    def sound(self,call):
        print(f"Cat says {call}")
class Dog():
    def sound(self,call):
        print(f"Dog says {call}")
c= Cat()
c.sound("Meow")
d= Dog()
d.sound("Bark")"""

"""39.  Create a Notification parent class and override send() in EmailNoti cation and SMS Notification

class Notification:
    def send(self,message):
        print("Sending Notification: ",message)
class EmailNotification(Notification):
        def send(self,message):
            print("Sending Email: ",message)
class SMSNotification(Notification):
    def send(self,message):
        print("Sending SMS: ",message)

n1 = EmailNotification()
n1.send("Your Order is Confirmed!")
n2 = SMSNotification()
n2.send("Your OTP is 6197")"""