# Since all the exception type we have a from the BaseException class.Hence, our exception should also inherit from the parent class itself

class FooException(Exception):
    pass
try:
    raise FooException("insert description here")
except FooException:
    print("A FooException was raised.")


a = FooException()
print(a)

# We can create a custom exception inheriting from a sub class of the BaseException class

class NegativeError(ValueError):
    pass

def foo(x):
 # function that only accepts positive values of x
    if x < 0:
        raise NegativeError("Cannot process negative numbers")
 # rest of function body
try:
    result = foo(int(input("Enter a positive integer: "))) # raw_input in Python 2.x
except NegativeError:
    print("You entered a negative number!")
else:
    print("The result was " + str(result))


a = foo(9)
print(a)

