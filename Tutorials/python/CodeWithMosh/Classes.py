# Classes: blueprint for creating new objects
# Objects: instance of a class

# Class: Human
# Object: John, Mary, Jack


# Creating Classes


class Point:
    def draw(self):
        print('draw')


point = Point()  # Returns a point object we can assign to a variable, in this case the variable is point
print(type(point))
print(isinstance(point, int))


# Constructors - special method that is called when we create new point object

class Point:
    # __init__ - magic method (this is a contrustor)   # self is a reference ot the current point object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point {self.x},{self.y}')


point = Point(1, 2)
point.draw()


# Class vs Instance Attributes


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point {self.x},{self.y}')


point = Point(1, 2)
point.draw()
point.default_color = "yellow"

print(point.default_color)
print(Point.default_color)

another = Point(3, 4)
print(another.default_color)
another.draw()

Point.default_color = "blue"
print(another.default_color)
print(point.default_color)


# Class vs Instance Methods

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f'Point {self.x},{self.y}')


point = Point.zero()
point.draw()


# Magic Methods

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def draw(self):
        print(f'Point {self.x},{self.y}')


point = Point(1, 2)
# Since if u do this wihtout magic method, it will return object at address. With magic method it will return the thing u want
print(point)


# Comparing Objects

class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def draw(self):
        print(f'Point {self.x},{self.y}')

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
another = Point(3, 4)
print(point > another)
