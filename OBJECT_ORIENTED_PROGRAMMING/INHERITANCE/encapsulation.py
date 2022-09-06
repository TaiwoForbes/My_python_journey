from item import Item

item1 = Item("Phone", 750,20)
print(item1.name)
# Trying to mask a new name will result in attribute error since the name attribute belongs to the @property decorator
# Setting a new Attribute
item1.name  = "Books"
print(item1.name) # AttributeError without using the @<name>.setter decorator, but it will if the @<name>.setter decorator is used
item1.increment(0.2)
print(item1.price)
item1.apply_discount()
print(item1.price)




