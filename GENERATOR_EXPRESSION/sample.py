# Generators are lazy iterators created by generator functions (using yield)
#Generator expressions are similar to list, dictionary and set comprehensions, but are enclosed with parentheses.
#The parentheses do not have to be present when they are used as the sole argument for a function call.

lst = [x ** 2 for x in range(10)]
print(lst) # List comprehenstion

gen = (x ** 2 for x in range(10))
print(gen) # Generator expression
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print()

# The above code for the generate works in the same way as the code below

for i in (x ** 2 for x in range(10)):
    print(i) # i iterate over the gen
print()

sum = sum(x for x in range(10) if x % 2 == 0)
print(sum)
print()

import itertools
natural_numbers = itertools.count(1)

multiples_of_two = (x * 2 for x in natural_numbers )
multiples_of_three = (x for x in natural_numbers if x % 3 == 0)
for x in (multiples_of_two):
    print(x)
    if x == 20:
        break
    

