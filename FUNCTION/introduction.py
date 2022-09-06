def append(elem, to = None):
    if to is None:
        to = []
        to.append(elem)
        return to
    else:
        to.append(elem)
        return to
element = 3
datatypes = []
print(append(element,datatypes))

# Nested function
def make_adder(n):
    def adder(x):
        return n + x
    return adder
add5 = make_adder(5)
print(add5(6)) # This should return 11