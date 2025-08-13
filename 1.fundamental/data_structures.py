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
