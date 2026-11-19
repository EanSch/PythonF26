#Imports created classes
from rectangle import Rectangle
from circle import Circle
from square import Square
from triangle import Triangle

# Create a list of shape objects
shapes = [
    Rectangle(10, 5),
    Circle(4),
    Square(6),
    Triangle(8, 4)
]

# Display the area of each shape
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area():.2f}")