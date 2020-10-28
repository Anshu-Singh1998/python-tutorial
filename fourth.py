# let us c
# The length and breadth of a rectangle and radius of circle are input through the keyboard.
# wap to calculate the area and perimeter of the rectangle and area  and circumference of circle.

length = int(input("Enter a length:"))
breadth = int(input("Enter a breadth:"))
radius = int(input("Enter a radius:"))
area = length*breadth
perimeter = 2 * (length+breadth)
circumference = 2*3.14*radius
area_of_circle = 3.14*radius*radius
print(area)
print(perimeter)
print(circumference)
print(area_of_circle)
