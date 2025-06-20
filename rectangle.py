from shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height, color="Black", position=(0, 0)):
        super().__init__(color)
        self.__width = width
        self.__height = height
        self.__position = position

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def is_square(self):
        return self.__width == self.__height

    def move(self, dx, dy):
        x, y = self.__position
        self.__position = (x + dx, y + dy)

    def describe(self):
        return f"Rectangle {self.__width}x{self.__height} at {self.__position}, color {self.get_color()}."
