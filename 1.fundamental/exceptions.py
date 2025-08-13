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
