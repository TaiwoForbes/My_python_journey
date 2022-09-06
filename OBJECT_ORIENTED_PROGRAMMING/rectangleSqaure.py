class Rectangle:
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def area(self):
        return (self.length * self.breath)

    def perimeter(self):
        return 2 * (self.length + self.breath)


class Square(Rectangle):
    def __init__(self, s):
        super(Square,self).__init__(s,s)
        self.s = s
        


rectangle = Rectangle(4, 2)
print(rectangle.area())
print(rectangle.perimeter())
sqaure = Square(2)
print(sqaure.area())
print(sqaure.perimeter())
