import time

print(time.time())


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
print(f"Emails sent in {end - start} seconds")
