def multiply(x,y):
    return sum(y for _ in range(x))

def multiply_better(x,y):
    if (x >= 0 and y >= 0)  or (x <= 0 and y <=  0):
        return sum(abs(y) for _ in range(abs(x)))
    elif x < 0:
        return sum(y for _ in range(x))
    else:
        return sum(y for _ in range(x))