def func(k, n = 0, arr = []):
    """This function recursively append a value n to a list"""
   
    if k == n:
        return 
    else:
        arr.append(n)
        func(k,n+1,arr)
        return arr
print(func(8))