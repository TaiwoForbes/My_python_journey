# A finally ensures the execution of a piece of code irrespective of the exception. 
# The use of finally is mostly noticed in a function || when defining a class

try:
    print("Hello world")
    a = int(input("ENTER A NUMBER : "))
    b = int(input("ENTER A NUMBER : ")) # since the tpye of a and b is int, any value aside int will be raise the except clause
    if b > 199:
        # The raise keyword is more like a custom exception, it is use when the try exception runs successfully
        raise Exception("Number is too large")
    print(a /b)
    
    # Specified exception type
except (ValueError):
    print("Value must be an integer")
except (ZeroDivisionError):
    print("A value can't be divided by zero")
    # Unspecified exception caught, but handled properly
except Exception as e:
    print(e)
# A finally ensures the execution of a piece of code irrespective of the exception
finally:
    print("Try was successful") # This will always be executed regardless of the exceptions
print("There were no error") # This will be printed even if the value type isnt meet. This is because the error was handled

