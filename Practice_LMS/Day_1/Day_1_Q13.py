"""Exercise 13 — Convert Minutes to Hours & Minute"""
minutes = int(input("Enter a time in minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Time is {hours}:{remaining_minutes}")