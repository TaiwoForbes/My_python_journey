def linear_search(list,target):
    """ 
    Returns the index position of the target if found,else return None
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None
    print('')


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}" )
    else:
        print("Target not found in list")

array = [1,2,3,4,5,6,7,8]
result = linear_search(array,7)
verify(result)