from datetime import datetime
log_error = lambda msg:(f"{datetime.now()} - ERROR - {msg}\n")
def write_error(msg):
    with open("error_log", "a") as file:
        file.write(log_error(msg))
for i in range(1,5):
    write_error(f"Sample Error Number {i}")
print("4 errors logged")
