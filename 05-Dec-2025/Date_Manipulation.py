from datetime import datetime,date,time,timedelta

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
now = datetime.now()
print(now)

dob = date(2025,12,5)
print(dob)

now = datetime.now()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)

next_week = today + timedelta(days=7)
yesterday = today - timedelta(days=1)
print(next_week)
print(yesterday)

start = date(2024,1,1)
end = date(2025,12,5)
diff = end - start
print(diff)

dt = datetime.combine(date(2025,12,5),time(10,3))
print(dt)