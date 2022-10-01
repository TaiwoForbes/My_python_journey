from die import Die

class Dice(Die):
    def __init__(self, numberOfSides,numberOfDice):
        super().__init__(numberOfSides)
        self.__numberOfDice = numberOfDice
        self.__dice = []
        self.__buildDice()


    def __buildDice(self):
        for _ in range(self.__numberOfDice):
            self.__dice.append(Die(self.__numberOfDice))

    def roll(self):
        for die in self.__dice:
            die.roll()
    def getValues(self):
        values = []
        for die in self.__dice:
            values.append(die.getValue())
        values.sort()
        return tuple(values)
    def getTotal(self):
        total = 0
        for die in self.__dice:
            total = total + die.getValue()
        return total

    def __str__(self) -> str:
        return str(self.getValues())