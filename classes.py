
#! Inheritance

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eating...")


class Mammal(Animal):
    def walk(self):
        print("Walking...")


class Fish(Animal):
    def swim(self):
        print("Swimming...")


m = Mammal()
m.eat()
print(m.age)

#! Properties and Decorators

# class Product:
#     def __init__(self, price: int):
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value: int):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value


# product = Product(100)
# # product.price = 200
# print(product.price)

# class Product:
#     def __init__(self, price: int):
#         self.__price = price

#     def __get_price(self):
#         return self.__price

#     def __set_price(self, value: int):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value
#     price = property(__get_price, __set_price)


# product = Product(100)
# # product.price = 200
# print(product.price)

#! Custom Container with Magic Methods

# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag: str):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag: str):
#         return self.tags.get(tag.lower(), 0)

#     def __setitem__(self, tag: str, count: int):
#         if count < 0:
#             raise ValueError("Count cannot be negative")
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)


# cloud = TagCloud()
# cloud.add('python')
# cloud.add('python')
# cloud.add('Python')
# print(cloud['python'])
# print(len(cloud))
# cloud['java'] = 3

# for index, tag in enumerate(cloud):
#     print(index, tag)

#! Custom Container with Magic Methods

# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag: str):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag: str):
#         return self.tags.get(tag.lower(), 0)

#     def __setitem__(self, tag: str, count: int):
#         if count < 0:
#             raise ValueError("Count cannot be negative")
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)


# cloud = TagCloud()
# cloud.add('python')
# cloud.add('python')
# cloud.add('Python')
# print(cloud['python'])
# print(len(cloud))
# cloud['java'] = 3

# for index, tag in enumerate(cloud):
#     print(index, tag)

#! add magic methods

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other: "Point"):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(10, 20)
# another = Point(1, 2)
# combined = point + another
# print(combined.x, combined.y)

#! Equality and Comparison Magic Methods

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other: "Point"):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other: "Point"):
#         return self.x > other.x and self.y > other.y


# point = Point(1, 2)
# another = Point(1, 2)
# another2 = Point(3, 4)
# print(point == another)
# print(point < another2)

#! Magic methods

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point at ({self.x}, {self.y})")


# point = Point(1, 2)
# print(point)

#! Class methods

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point at ({self.x}, {self.y})")


# point = Point.zero()

# point.draw()

#! class attributes

# class Point:

#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point at ({self.x}, {self.y})")


# Point.default_color = "blue"

# point = Point(1, 2)
# print(Point.default_color)

# point.draw()

# another = Point(3, 4)
# print(another.default_color)
# another.draw()

#! Constructor

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point at ({self.x}, {self.y})")


# point = Point(1, 2)

# point.draw()
