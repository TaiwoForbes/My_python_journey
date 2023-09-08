def binary_search(list,target):
    first = 0 
    last = len(list) - 1

    for i in range(0,len(list)):
      midpoint = (first + last) // 2  
      if list[midpoint] == target:
        return midpoint
      elif list[midpoint] < target:
        first = midpoint + 1
      else:
        last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}" )
    else:
        print("Target not found in list")


array = [num for num in range(1,20+1)]
print(array)
result = binary_search(array,8)
verify(result)