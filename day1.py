"""
Calculate are of circle, rectangle and square after taking values from the user
"""
radius = float(input("Enter the value of radius: \n"))
area = 3.14 * radius * radius
length = float(input("Enter the value for length: \n"))
width = float(input("Enter the value for width: \n"))
area1 = length * width

if length == width:
    print("Area of square:",area1)
else:
    print("Area of rectangle:",area1)

print("Area of circle =",area)

