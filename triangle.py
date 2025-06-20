from shape import Shape
import math


class Triangle(Shape):
    def __init__(self, side1, side2, side3, triangle_type="scalene", color="Black"):
        super().__init__(color)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        self.__type = triangle_type

    def perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def triangle_type(self):
        return self.__type

    def scale(self, factor):
        self.__side1 *= factor
        self.__side2 *= factor
        self.__side3 *= factor

    def describe(self):
        return f"{self.__type.capitalize()} triangle with sides {self.__side1}, {self.__side2}, {self.__side3}, color {self.get_color()}."

