from datetime import datetime,date,time,timedelta

"""11. Given a customer’s subscription start date and duration (in days), compute expiry date.
start_date = date(2025,12,3)
duration = 30
expiry_date = start_date+timedelta(days=duration)
print("Subscription expiring on : ",expiry_date)"""

"""12.Given two dates (start_date, end_date), write a function that returns the number of weekdays.
start_date = date(2025,12,3)
end_date = date(2026,2,14)

def weekdays(start_date, end_date):
    if start_date>end_date:
        start_date, end_date = end_date, start_date
    count = 0
    day = start_date
    while day<=end_date:
        if day.weekday()<5:
            count += 1
        day += timedelta(days=1)
    return count
print("No. of weekdays: ",weekdays(start_date, end_date))"""

"""13. You are given a list of attendance timestamps. Count how many fall on a Monday.

attendance_timestamps = [
    "2025-11-24 09:05:12",
    "2025-11-24 17:32:45",
    "2025-11-25 09:12:08",
    "2025-11-25 17:28:30",
    "2025-11-26 09:03:55",
    "2025-11-26 17:35:10",
    "2025-11-27 09:10:20",
    "2025-11-27 17:40:05",
    "2025-11-28 09:07:45",
    "2025-11-28 17:33:50"
]
count=0
for ts in attendance_timestamps:
    date = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    if date.weekday() == 0:
        count+=1
print("No. of mondays : ",count)"""

"""14. Write a function that checks if a given date is in the future, past, or today.
def check(input_date):
    if isinstance(input_date,str):
        input_date = datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S").date()
    today = datetime.now().date()
    #input_date = input_date.date()

    if input_date < today:
        print("Input date is in the past")
    elif input_date > today:
        print("Input date is in the future")
    elif input_date == today:
        print("Input date is today")
check("2025-11-24 09:05:12")"""

"""15. Given a delivery date and expected delivery timeline (like 3 days), calculate estimated delivery
date.
def estimated_deltime(start_date,days):
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    return start_date + timedelta(days=days)
print("Estimated Delivery Time")
print(estimated_deltime("2025-12-3",10))"""

"""17. Write a function that returns True if a given year is a leap year.
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
print(is_leap_year(2025))"""

"""18. Given a list of expiry dates, find which products expire within the next 15 days.
def expiry_soon(dates):
    today = date.today()
    end_date = today + timedelta(days=15)
    verdict = []
    for d in dates:
        if isinstance(d,str):
            d = datetime.strptime(d, "%Y-%m-%d").date()
        if today <=d <=end_date:
            verdict.append(d)
    return verdict
expiry_dates = ["2026-01-10","2025-12-17","2025-12-14"]
print("Expiring soon")
print(expiry_soon(expiry_dates))"""

"""19. Convert a list of date strings into datetime objects and sort them.
def sort_dates(d_list):
    converted = [d.strftime("%Y-%m-%d") for d in d_list]
    return sorted(converted)
dates = ["2024-05-10","2003-10-11","2014-08-27"]
print(sort_dates(dates))"""

"""20. Generate a list of dates for the next 30 days starting from today.
def next_30():
    l=[]
    today = date.today()
    return [today + timedelta(days=i) for i in range(30)]
print("Print the next 30 days")
print(next_30())"""
