shape = input()
from math import pi

if shape == "square":
    square_sides = float(input())
    shape_area = square_sides * square_sides

elif shape == "rectangle" :
    rectangle_height = float(input())
    rectangle_sides = float(input())
    shape_area = rectangle_height * rectangle_sides

elif shape == "circle" :
    circle_radius= float(input())
    shape_area = pi * circle_radius * circle_radius

elif shape == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    shape_area = (triangle_side * triangle_height) / 2


print(f"{shape_area:.3f}")
