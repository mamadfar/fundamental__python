
import random
import string

print(random.random() * 100)
print(random.randint(1, 100))
print(random.choice([1, 2, 3, 4, 5]))
print("".join(random.choices("abcdefghijk", k=4)))
print("".join(random.choices(string.ascii_letters + string.digits, k=8)))
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
