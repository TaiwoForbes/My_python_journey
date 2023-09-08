def recursiveBinarySearch(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
               return recursiveBinarySearch(list[midpoint+1:], target) #Slicing: by discarding the left portion of the list
            else:
                return recursiveBinarySearch(list[:midpoint],target) #Slicing: by discarding the right portion of the list

def verify(result):
        print(f"Target found: {result}" )

number = [num for num in range(1,200+1) ]
result = recursiveBinarySearch(number,4)
verify(result)
print('')
result = recursiveBinarySearch(number,201)
verify(result)