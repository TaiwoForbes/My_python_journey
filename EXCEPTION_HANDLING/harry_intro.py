from logging import raiseExceptions


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
# The else clause will be executed if the try block is executed successfully

else:
    print("Try was successful")
print("There were no error") # This will be printed even if the value type isnt meet. This is because the error was handled
