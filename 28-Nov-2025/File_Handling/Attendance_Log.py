""" 3. Attendance Log Writer
 For each student name given by the user, append an entry to attendance.log with timestamp and
 status (Present/Absent)"""

from datetime import datetime
atd_log = lambda name,status : f"{datetime.now()} - {name} - {status}\n"
while True:
    print("Enter STOP to end\n")
    name = input("Enter NAME: ")
    if name.lower() == "stop":
        break

    status = input("Enter STATUS (Present/Absent): ")

    with open("attendance_log.txt", "a") as f:
        f.write(atd_log(name, status))
print("Attendance Recorded")
