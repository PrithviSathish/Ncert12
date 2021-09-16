import math

# TYPE 1

# Circle
def circle_area(radius):
    return math.pi * (radius ** 2)

def circle_perimeter(radius):
    return 2 * math.pi * radius

# Square
def square_area(side):
    return side ** 2

def square_area(side):
    return 4 * side

# Rectangle
def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)


# TYPE 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circle_perimeter(self):
        return 2 * math.pi * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def square_area(self):
        return self.side ** 2

    def square_area(self):
        return 4 * self.side


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def rectangle_area(self):
        return self.length * self.breadth

    def rectangle_perimeter(self):
        return 2 * (self.length + self.breadth)