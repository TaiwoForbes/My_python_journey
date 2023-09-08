def sumOfN(num):
    """
    This function calculates the sum of first n natural number recursively
    """

    if num == 1 or num == 0:
        return 1
    
    else:
        
        return num + sumOfN(num - 1)
    
print(sumOfN(4))