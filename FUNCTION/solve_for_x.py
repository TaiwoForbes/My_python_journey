def solveEqn(equation):
    """ This function return the value for x"""
    num1, add, x, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    return "x = " + str(num2 - num1)


print(solveEqn("4 + x = 9"))
print(solveEqn.__doc__)
