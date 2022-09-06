arr = [1, 2, 3, 4, 5]
length = int(len(arr)/2)
initial_length = len(arr)

for i in range(length):
    tmp = arr[i]
    arr[i] = arr[initial_length - 1 - i]
    arr[initial_length - 1 - i] = tmp
print(arr)
