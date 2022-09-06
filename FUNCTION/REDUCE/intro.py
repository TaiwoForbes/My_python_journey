# Reduce takes a function and a collection of items. It returns a value that is created by combining the items
from functools import reduce


list = [0,1,2,3,4,5]
total = reduce(lambda a, x: a + x, list)
print(total) 