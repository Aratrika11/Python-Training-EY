class Notification:
    def send(self,message):
        print("Sending Notification: ",message)
class EmailNotification(Notification):
        def send(self,message):
            print("Sending Email: ",message)
class SMSNotification(Notification):
    def send(self,message):
        print("Sending SMS: ",message)
class PushNotification(Notification):
    def send(self,message):
        print("Sending Push: ",message)

n1 = EmailNotification()
n1.send("Your Order is Confirmed!")
n2 = SMSNotification()
n2.send("Your OTP is 6197")
n3 = PushNotification()
n3.send("You have a new message")