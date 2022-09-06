import math
def getArea(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle()
    elif shape == "circle":
        circle()
    else:
        print("This only calculate the area of a rectangle and a circle")

def rectangle():
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    print("The area of the rectangle is {}".format(length * width))
def circle():
    radius = float(input("Enter your radius"))
    area = math.pi * (math.pow(radius,2))
    print("The area of the cirlce is {:.2f}".format(area))


if "__main__" == __name__:
    shapeType = input("Enter you desired shape to calculate the area: ")
    getArea(shapeType)