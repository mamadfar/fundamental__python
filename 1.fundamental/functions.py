# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input

# print(fizz_buzz(4))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print('start')
# print(multiply(2, 3, 4))

# message = 'a'

# def change_message():
#     global message
#     message = 'b'

# change_message()
# print(message)

# def save_user(**user):
#     print(user['id'])
#     print(user['name'])
#     print(user['age'])
#     print(user['city'])
#     print(user)

# save_user(id=1, name="Mohammad", age=30, city="Tehran")

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2, 3, 4))

# def increment(number, by=1):
#     return number + by

# print(increment(2))

# def increment(number, by):
#     return number + by

# print(f"Incremented result: {increment(number=2, by=1)}")

# def greet(first_name, last_name):
#     print(f"Hello {first_name} {last_name}!")
#     print("Welcome to Python programming.")

# greet("Mohammad", "Farhadi")
# greet("John", "Doe")

# def get_greeting(name):
#     return f"Hello {name}!"

# message = get_greeting("Mohammad")
# print(message)
# file = open("message.txt", "w")
# file.write(message)
# file.close()

# def greet():
#     print("Hi there!")
#     print("Welcome to Python programming.")

# greet()
