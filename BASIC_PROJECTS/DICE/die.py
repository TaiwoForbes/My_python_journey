import random

# class Die


class Die:
    MIN_SIDES = 2
    MAX_SIDES = 120

    def __init__(self, numberOfSides):
        # - numberOfSides : intergers
        if not isinstance(numberOfSides,int):
            raise TypeError("Value must be an integer")
        else:
            self.__numberOfSides = numberOfSides
        # - value : integer
        self.__value = 0
        # end of method
    # end of method
    @property
    def numberOfSides(self):
        return self.__numberOfSides

    @numberOfSides.setter
    def numberofside(self,value):
        self.__numberOfSides = value

    # + setNumberOfSides() : void
    def setNumberOfSdies(self, numberOfSides):
        if numberOfSides >= self.MIN_SIDES and numberOfSides <= self.MAX_SIDES:
            self.__numberOfSides = numberOfSides
    # end of method

    # + getNumberOfSides() + Integer
    def getNumberOfsides(self):
        return self.__numberOfSides
    # end of method

    # + getValue() : integer
    def getValue(self):
        return self.__value
    # end of method

    # + roll() : void
    def roll(self):
        self.__value = random.randint(1, self.__numberOfSides)
    # end of method

    # + toString() : string
    def __str__(self):
        return str(self.getValue())

# end of class