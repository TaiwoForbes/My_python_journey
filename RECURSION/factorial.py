def factorial(num):
    """
    This function calculates the factorial of a given recursively
    """

    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        
        return num * factorial(num - 1)

print(factorial(7))
    