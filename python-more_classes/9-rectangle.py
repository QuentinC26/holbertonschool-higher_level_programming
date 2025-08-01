#!/usr/bin/python3
"""Rectangle Class.

Rectangle class is a class that represents a rectangle but is empty.
"""


class Rectangle:
    '''
    Rectangle Class.

    Rectangle class is a class that represents a rectangle but is empty.
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        line = ""
        list_of_height = []
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for horizontal in range(self.height):
                line = str(self.print_symbol) * self.width
                list_of_height.append(line)
            return "\n".join(list_of_height)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        width = 0
        height = 0
        if not rect_1:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if not rect_1:
            raise TypeError("rect_1 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 == area_2:
            return rect_1
        elif area_1 > area_2:
            return rect_1
        elif area_2 < area_1:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
