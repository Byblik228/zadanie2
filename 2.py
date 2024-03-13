################Библиотека#################
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def is_right_triangle(self):
        sides = sorted([self.side_a, self.side_b, self.side_c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
###################Вычисление площади###############
def print_area(shape):
    print(shape.area())

circle = Circle(8)
triangle = Triangle(4, 4, 5)

print_area(circle)
print_area(triangle)

#################Юнит-тесты#################
import unittest

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(8)
        self.assertAlmostEqual(circle.area(), 201.06192982974676)

    def test_triangle_area(self):
        triangle = Triangle(4, 4, 5)
        self.assertAlmostEqual(triangle.area(), 7.806247497997997)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

if __name__ == '__main__':
    unittest.main()
