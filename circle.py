from shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius, space="2D", color="Black", center=(0, 0)):
        super().__init__(color)
        self.__radius = radius
        self.__space = space
        self.__center = center

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def diameter(self):
        return 2 * self.__radius

    def move_center(self, x, y):
        self.__center = (x, y)

    def describe(self):
        return f"Circle with radius {self.__radius}, center {self.__center}, color {self.get_color()}."
