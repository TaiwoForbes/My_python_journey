"""
Create a class pets from a class Animals and further create a class
Dog from from Pets. Add a method bark to class Dog
"""


class Animal:
    pass


class Pet(Animal):
    pass


class Dog(Pet):
    def bark(self):
        print("WOOF WOOF!")
bingo = Dog()
bingo.bark()
    

