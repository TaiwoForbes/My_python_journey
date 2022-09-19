# RAISE EXCEPTION
"""
f your code encounters a condition it doesn't know how to handle, such as an incorrect parameter, it should raise
the appropriate exception.
"""
def even_the_odds(odds):
    if odds % 2 != 1:
        raise ValueError("Did not get an odd number")
    return odds + 1
print(even_the_odds(3))