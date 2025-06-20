class Shape:
    def __init__(self, color=0):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):

        self.__color = color

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def describe(self):
        return f"This shape has color {self.__color}"