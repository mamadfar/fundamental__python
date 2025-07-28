from datetime import datetime, timedelta

dt1 = datetime(2023, 10, 1, 12, 0, 0)
dt2 = datetime(2023, 10, 1, 12, 0, 0) + timedelta(days=1, hours=2, minutes=30)
print(f"dt2: {dt2}")
now = datetime.now()

duration = now - dt1
print(f"Duration: {duration}")
print(f"Days: {duration.days}")
print(f"Seconds: {duration.seconds}")
print(f"Total seconds: {duration.total_seconds()}")
