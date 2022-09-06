def greatest(a,b,c):
    """
    This function finds the greatest of three numbers
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
print(greatest(3222,622,21))