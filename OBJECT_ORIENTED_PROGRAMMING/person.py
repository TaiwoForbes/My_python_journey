class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    @classmethod
    def from_full_name(cls, name, age):
        if " " not in name:
            raise ValueError
        first_name, last_name = name.split(" ", 2)
        return cls(first_name, last_name, age)
    def __repr__(self):
        return "Hello, my name is " + self.full_name + "." + " I'm " + str(self.age) + " years old"
    def greet(self):
        print("Hello, my name is " + self.full_name + "." + " I'm " + str(self.age) + " years old")


bob = Person('Taiwo','Soyemi', 19)
"""print(bob.greet())"""
print(Person.from_full_name('Taiwo Soyemi', 19))
print(type(Person))