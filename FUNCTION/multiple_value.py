


def multi(num1,num2):
    """This function return two different results"""
    return (num1 * num2) , (num1 / num2)

# When calling the function with one variable, the variable perform the works of the two return statement.
one_variable = multi(9,3) 
print(one_variable) # This will print 27 and 3 for just one variable since only one is provided
print()

# When calling the function with two different variable, two different result the respective variable
Variable1, Variable2 = multi(12,3)
print(Variable1,Variable2)
print("12 * 3 = {}\n12 / 3 = {}".format(Variable1,Variable2))

