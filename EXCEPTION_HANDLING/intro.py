"""
Errors detected during execution are called exceptions and are not unconditionally fatal. Most exceptions are not
handled by programs; it is possible to write programs that handle selected exceptions. There are specific features
in Python to deal with exceptions and exception logic.

Note : exceptions have a rich type hierarchy, all inheriting from the BaseException type.

"""
# Catching multiple exceptions

try:
    d = {}
    a = d[1]
    b = d.non_existing_field
except (KeyError, AttributeError) as e:
    print("A KeyError or an AttributeError exception has been caught.")
print()
print()

# Creating a seperate blocks for exception caught
try:
    d = {}
    a = d[1]
    b = d.non_existing_field
except KeyError as e:
    print("A KeyError has occurred. Exception message:", e)
except AttributeError as e:
    print("An AttributeError has occurred. Exception message:", e)
print()
print()



"""
Exception handling occurs based on an exception hierarchy, determined by the inheritance structure of the
exception classes.

For example, IOError and OSError are both subclasses of EnvironmentError. Code that catches an IOError will not
catch an OSError. However, code that catches an EnvironmentError will catch both IOErrors and OSErrors.
"""

# ELSE
'''
Code in an else block will only be run if no exceptions were raised by the code in the try block. This is useful if you
have some code you don’t want to run if an exception is thrown, but you don’t want exceptions thrown by that
code to be caught.
'''
'''try:
    data = {1: 'one', 2: 'two'}
    print(data[1])
except KeyError as e:
    print('key not found')
else:
    raise ValueError()'''


# Chain exceptions with raise from
"""
In the process of handling an exception, you may want to raise another exception. For example, if you get an
IOError while reading from a file, you may want to raise an application-specific error to present to the users of your
library, instead.
"""

try:
    5 / 0
except ZeroDivisionError as e:
    raise ValueError("Division failed") from e

