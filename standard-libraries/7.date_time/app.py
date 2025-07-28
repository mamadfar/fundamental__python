
from datetime import datetime
from time import time

dt1 = datetime(2023, 10, 1, 12, 0, 0)
now = datetime.now()  # Current date and time
print(dt1)  # Specific date and time
print(now)
# Convert string to datetime
dt2 = datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
print(dt2)
# or
# Convert string to datetime with different format
dt3 = datetime.strptime("2023/10/01 12:00:00", "%Y/%m/%d %H:%M:%S")
print(dt3)

dt4 = datetime.fromtimestamp(time())  # Convert timestamp to datetime
print(dt4)

print(f"{dt4.year}-{dt4.month:02}-{dt4.day:02} {dt4.hour:02}:{dt4.minute:02}:{dt4.second:02}")

print(dt4.strftime("%Y-%m-%d %H:%M:%S"))

print(now > dt1)  # Compare two datetime objects
