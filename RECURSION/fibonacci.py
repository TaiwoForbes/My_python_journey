def fibonacci(num):
    """
    This function calculates the fibonnaci of a given number recursively
    """

    if num == 0:
        return 0

    elif num == 1:
        return 1

    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(2))
