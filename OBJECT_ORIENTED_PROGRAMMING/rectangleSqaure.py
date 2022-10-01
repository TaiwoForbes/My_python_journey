class Square:
    def __init__(self, width="0", height="0"):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Enter a valid number")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Enter a valid number")

    def getArea(self):
        return int(self.__height) * int(self.__width)

    def perimeter(self):
        return 2 * int(self.__width) + int(self.__height)


if __name__ == "__main__":
    square1 = Square()
    height = input("Enter height: ")
    width = input("Enter width: ")

    square1.width = width
    square1.height = height

    print(square1.getArea())
    print(square1.perimeter())
