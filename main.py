from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from square import Square


def TotalArea(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

circle = Circle(radius=6, color="Black", center=(2, 3))
rectangle = Rectangle(width=4, height=6, color="Blue", position=(0, 0))
triangle = Triangle(side1=3, side2=4, side3=5, triangle_type="right", color="Green")
square = Square(side1=5, side2=5)

print(circle.describe())
print(f"Circle area: {circle.area():.2f}, perimeter: {circle.perimeter():.2f}, diameter: {circle.diameter()}\n")

print(rectangle.describe())
print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}, is square: {rectangle.is_square()}\n")

print(triangle.describe())
print(f"Triangle area: {triangle.area():.2f}, perimeter: {triangle.perimeter()}, type: {triangle.triangle_type()}\n")

print(square.describe())

my_rectangle_shape = Square(side1=4, side2=6, color="Blue", position=(10, 20))
print(my_rectangle_shape.describe())



shapes = [circle, rectangle, triangle]

print(f"Total area of all shapes: {TotalArea(shapes):.2f}")

print(f"Circle > Rectangle: {circle > rectangle}")
print(f"Triangle < Square: {triangle < rectangle}")