
#! Data classes

# # * --------- Way 1 ---------
# from collections import namedtuple


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other: "Point"):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)

# # * --------- Way 2 ---------
# Point = namedtuple("Point", ["x", "y"])

# p1 = Point(x=1, y=2)
# p2 = Point(x=1, y=2)
# print(p1 == p2)

#! Extending built-in types

class Text(str):
    def duplicate(self):
        return self + self


text = Text("Hello ")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print(f"Adding {object} to the list")
        super().append(object)


trackable_list = TrackableList()
trackable_list.append(1)

#! Polymorphism and Interfaces

# class Shape:
#     def area(self):
#         """Calculate the area of the shape."""
#         raise NotImplementedError("Subclasses must implement this method")


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side


# def print_area(shapes: list[Shape]):
#     for shape in shapes:
#         if isinstance(shape, Shape):
#             print(f"Area: {shape.area()}")
#         else:
#             print("Invalid shape type")


# print_area([Circle(5), Square(4)])

#! Abstract Base Classes

# from abc import ABC, abstractmethod


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is not opened")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         """Read data from the stream."""
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading from file stream")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading from network stream")


# class MemoryStream(Stream):
#     def read(self):
#         print("Reading from memory stream")


# stream = MemoryStream()
# stream.open()

#! Exceptions and inheritance
# class InvalidOperationError(Exception):
#     pass


# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is not opened")
#         self.opened = False


# class FileStream(Stream):
#     def read(self):
#         print("Reading from file stream")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading from network stream")

#! Super() and Inheritance

# class Animal:
#     def __init__(self):
#         print("Animal created")
#         self.age = 1

#     def eat(self):
#         print("Eating...")


# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Mammal created")
#         self.weight = 10

#     def walk(self):
#         pass


# m = Mammal()
# m.eat()
# print(m.age)


#! Inheritance

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("Eating...")


# class Mammal(Animal):
#     def walk(self):
#         print("Walking...")


# class Fish(Animal):
#     def swim(self):
#         print("Swimming...")


# m = Mammal()
# m.eat()
# print(m.age)
# print(isinstance(m, Animal))
# print(isinstance(m, Mammal))
# print(isinstance(m, Fish))
# print(isinstance(m, object))
# print(issubclass(Mammal, Animal))
# print(issubclass(Mammal, object))

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
