"""
Python programming practice exercises.
This module contains various examples and exercises for learning Python basics.
"""

#! Exception Handling Example

from timeit import timeit


code1 = """
def calculate_xfactor(age: int):
    if age <= 0:
        raise ValueError('Age must be greater than zero.')
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as err:
    pass
"""

code2 = """
def calculate_xfactor(age: int):
    if age <= 0:
        return None
    return 10 / age


    xfactor = calculate_xfactor(-1)
    if xfactor is None:
        pass
"""

print("First code= ", timeit(code1, number=10000))
print("Second code= ", timeit(code2, number=10000))

# def calculate_xfactor(age: int):
#     if age <= 0:
#         raise ValueError('Age must be greater than zero.')
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as err:
#     print(err)

# try:
#     with open('app.py') as file, open('app2.py') as file2:
#         print(file.read())
#         print(file2.read())
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as err:
#     print("Invalid input. Please enter a valid age.")
#     print(err)

# try:
#     file = open('app.py')
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as err:
#     print("Invalid input. Please enter a valid age.")
#     print(err)
# else:
#     if age >= 18:
#         print("You are an adult.")
#     else:
#         print("You are a minor.")
# finally:
#     file.close()
#     print("File closed successfully.")
# print("Thank you for using the program.")

# nums = [1, 2]
# print(nums[3])


#! Most Frequent Character in a String
# from pprint import pprint

# sentence = "This is a common interview question"


# # ? Way 1 ----------------------------------
# def most_frequent_char(txt: str) -> dict[str, int]:
#     return {char: txt.count(char) for char in txt}

# # print(max(most_frequent_char(sentence), key=most_frequent_char(sentence).get))


# sorted_chars = sorted(most_frequent_char(sentence).items(),
#                       key=lambda kv: kv[1], reverse=True)

# print(sorted_chars[0])
# # pprint(sorted_chars, width=10)

# # ? Way 2 ----------------------------------
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# sorted_char_frequency = sorted(
#     char_frequency.items(), key=lambda kv: kv[1], reverse=True)
# print(sorted_char_frequency[0])
# pprint(sorted_char_frequency, width=10)

# def most_frequent_char(txt):

# most_frequent_char(sentence)

# first_dict = {'a': 1, 'b': 2}
# second_dict = {'a': 10, 'd': 4}

# print({**first_dict, **second_dict, 'z': 5})  # Merging two dictionaries

# values = list(range(5))
# print(*values)

# print([*range(5), *'mamad'])

# first = [1, 2, 3]
# second = [4, 5, 6]

# print([*first, 'a', *second, *'mamad'])  # Merging two lists

# nums = [1, 2, 3, 4, 5]
# print(*nums)  # Unpacking the list to print elements

#! Generator expression example
# from sys import getsizeof

# values = (x*2 for x in range(1000000))
# print(f"Size of generator: {getsizeof(values)} bytes")
# # print(len(values))
# values = [x*2 for x in range(1000000)]
# print(f"Size of list: {getsizeof(values)} bytes")

# values = (x*2 for x in range(10))

# for value in values:
#     print(value)

#! Data types comprehension example
# values = []
# for x in range(5):
#     values.append(x * 2)

# print([x * 2 for x in range(5)])  # List comprehension
# print({x * 2 for x in range(5)})  # Set comprehension
# print({x: x * 2 for x in range(5)})  # Dictionary comprehension
# print((x * 2 for x in range(5)))  # Generator expression

#! Dictionaries example
# point = {'x': 1, 'y': 2}
# point = dict(x=1, y=2)
# print(point['x'])
# point['z'] = 3
# print(point)

# if 'a' in point:
#     print("Key 'a' exists in the dictionary")
# print(point.get('a', 'Key not found'))

# del point['x']
# print(point)

# for key, value in point.items():
#     print(key, value)

#! Sets example
# nums = [1, 1, 2, 3, 4, 4]
# first = set(nums)
# print(first)  # Convert list to set to remove duplicates
# second = {1, 5}
# print(first | second)  # Union of two sets
# print(first & second)  # Intersection of two sets
# print(first - second)  # Difference of two sets - elements in first not in second
# print(second - first)  # Difference of two sets - elements in second not in first
# print(first ^ second)  # Symmetric difference of two sets

# if 1 in first:
#     print("1 is in the set")

#! array module example
# from array import array

# nums = array('b', [1, 2, 3])
# nums.append(4)
# print(list(nums))

#! Swapping variables
# x = 10
# y = 11

# x, y = y, x
# print(f"x: {x}, y: {y}")

# from collections import deque

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# queue.popleft()
# print(queue)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(list(zip('abc', list1, list2)))

# items = [
#     ('item1', 41),
#     ('item2', 80),
#     ('item3', 30),
# ]

# prices = [item[1] for item in items]
# print(prices)

# filtered_items = [item for item in items if item[1] < 50]
# print(filtered_items)

# items = [
#     ('item1', 41),
#     ('item2', 80),
#     ('item3', 30),
# ]

# filtered_items = list(filter(lambda item: item[1] < 50, items))
# print(filtered_items)

# items = [
#     ('item1', 41),
#     ('item2', 80),
#     ('item3', 30),
# ]

# prices = list(map(lambda item: item[1], items))
# print(prices)

# items = [
#     ('item1', 41),
#     ('item2', 80),
#     ('item3', 30),
# ]

# def sort_by_price(item):
#     return item[1]

# print(sorted(items, key=sort_by_price))
# items.sort(key=sort_by_price)
# items.sort(key=lambda item: item[1])
# print(items)

# nums = [53, 10, 40, 2, 1, 8]
# # nums.sort(reverse=True)
# print(sorted(nums))
# print(nums)

# chars = ['a', 'b', 'c', 'd', 'e']

# print(chars.count('a'))

# if 'z' in chars:
#     print(chars.index('z'))

# chars = ['a', 'b', 'c', 'd', 'e']

# chars.append('f')
# print(chars)
# chars.insert(0, '-')
# print(chars)
# chars.pop(1)
# print(chars)
# chars.remove('d')
# print(chars)
# del chars[1:3]
# print(chars)
# chars.clear()
# print(chars)

# chars = ['a', 'b', 'c', 'd', 'e']

# for char in enumerate(chars):
#     print(f"Index: {char[0]}, Value: {char[1]}")
#     print(char)

# nums = list(range(1, 11))
# first, second, third, *rest = nums
# print(f"First: {first}, Second: {second}, Third: {third}, Rest: {rest}")

# first, *rest, last = nums
# print(f"First: {first}, Rest: {rest}, Last: {last}")

# letters = ['a', 'b', 'c', 'd', 'e']
# numbers = list(range(20))
# print(numbers[::-1])
# copyLetters = letters[:]
# print(letters, copyLetters)

# letters = ['a', 'b', 'c', 'd', 'e']
# matrix = [[1, 2], [3, 4]]
# zeros = [0] * 5
# print(zeros)
# combined = zeros + letters
# print(combined)
# nums = list(range(20))
# print(nums)
# chars = list('mamad')
# print(len(chars))

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

# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         print(number)
#         count += 1
# print(f"We have {count} even numbers.")

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == 'quit':
#         break

# command = ""

# while command.lower() != 'quit':
#     command = input(">")
#     print("ECHO", command)

# while number > 0:
#     print("Hello World", number)
#     number //= 2

# for x in "Python":
#     print(x, end='-')
# print('\n')
# for x in [1, 2, 3, 4, 5]:
#     print(x, end='-')

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})", end='-')

# successful = False
# for number in range(1, 4):
#     print("Hello World", number)
#     if successful:
#         print("Success")
#         break
# else:
#     print("Failed", number, "times")

# for number in range(1, 5):
#     for j in range(1, 5):
#         print("Hello World", number, j * '*')

# for number in range(3, 12, 3):
#     print("Hello World", number)

# if 10 == "10":
#     print("Equal")
# elif "bag" > "cat" and "bag" > "apple":
#     print("Bag is the largest")
# else:
#     print("No match found")

# age = 22
# if age >= 18 and age < 65:
# if 18 <= age < 65:
#     print("Eligible")

# high_income = False
# good_credit = True
# student = True

# if high_income or good_credit:
# if not student:
# if (high_income or good_credit) and not student:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# age = 22

# if age >= 18:
#     message = 'You are an adult'
# else:
#     message = 'You are a minor'

# message = "Eligible" if age >= 18 else "Not eligible"

# print(message)

# temperature = 30

# if temperature > 30:
#     print('It is a hot day')
# elif temperature < 10:
#     print('It is a cold day')
# else:
#     print('It is a lovely day')

# print(10 >= 3)
# print(10 == "10")
# print('bag' > 'apple')
# print(ord('a'))
# print(ord('A'))

# print(bool(0))
# print(bool(""))
# print(bool(None))
# print(bool([]))
# print(bool({}))

# x = input("x: ")
# print(type(x))
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# from math import ceil, floor, sqrt

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)  # Floor division
# print(10 % 3)  # Modulus
# print(10 ** 3)  # Exponentiation

# print(round(2.9))
# print(abs(-2.9))
# print(ceil(2.2))
# print(floor(2.9))
# print(sqrt(16))

# student_count = 1000
# print("Student count:", student_count)
# rating = 4.5
# print("Rating:", rating)
# is_published = True
# print("Is published:", is_published)
# course_name = "Python Programming"
# print("Course name:", course_name)

# message = """Welcome to the course!
# This course will teach you Python programming from scratch.
# You will learn about variables, data types, control structures, functions, and more."""
# print("Message:", message)

# print(len(course_name))
# print(course_name[0])
# print(course_name[-1])
# print(course_name[0:6])
# print(course_name[7:])
# print(course_name[:6])
# print(course_name[7:17])
# print(course_name[0:6:2])
# print(course_name[::2])
# print(course_name[:])

# first = "Mohammad"
# last = "Farhadi"
# full = f"{first} {last}"
# print("Full name:", full)

# course = "   Python programming   "

# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.lstrip())
# print(course.rstrip())
# print(course.find('pro'))
# print(course.lower().replace('p', 'j'))
# print('Python' in course)
# print('mamad' not in course)
