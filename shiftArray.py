def shift_array(array,s):
    s %= len(array)
    s *= -1
    shifted_array = array[s:] + array[:s]
    return shifted_array


arr = [1,2,3,4]
shift = shift_array(arr,2)
print(shift)