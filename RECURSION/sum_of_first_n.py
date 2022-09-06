def sumOfN(num):
    """
    This function calculates the sum of first n natural number recursively
    """

    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        
        return num + sumOfN(num - 1)
    
        

print(sumOfN(3))