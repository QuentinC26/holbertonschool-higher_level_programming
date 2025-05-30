#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        if self.radius < 0:
            return math.pi * abs(self.radius) ** 2
        return math.pi * self.radius ** 2

    def perimeter(self):
        if self.radius < 0:
            return math.pi * abs(self.radius) ** 2
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2*(self.height + self.width)


def shape_info(shape):
    print("Area: {}".format(shape.area))
    print("Perimeter: {}".format(shape.perimeter))
