from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side1, side2, color="Black", position=(0, 0)):
        super().__init__(width=side1, height=side2, color=color, position=position)
        self.__side1 = side1
        self.__side2 = side2

    def get_sides(self):
        return (self.__side1, self.__side2)

    def is_square(self):
        return self.__side1 == self.__side2

    def describe(self):
        shape_type = "Square" if self.is_square() else "Rectangle-like"
        return f"{shape_type} with sides {self.__side1} and {self.__side2} at {self._Rectangle__position}, color {self.get_color()}."

