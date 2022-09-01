lst = [x ** 2 for x in range(10)]
print(lst) # List comprehenstion

gen = (x ** 2 for x in range(10))
print(gen) # Generator expression
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# The above code for the generate works in the same way as the code below

for i in (x ** 2 for x in range(10)):
    print(i) # i iterate over the gen
    print(type(i))