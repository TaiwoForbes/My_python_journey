from array import *
my_array = array('i', [1,2,3,3,3,4,5]) 
print(my_array[1]) 
print(my_array[2]) 
print(my_array[0])

print(type(my_array))

#Append any value to an  array using the append method

my_array.append(9)
print(my_array)

# Insert any value using the insert method

my_array.insert(2,10) # Note the insert moethod takes two arguements
print(my_array)

# Extend an array using the extend method
second_array = array('i', [23,49,90,60,81])
my_array.extend(second_array)
print(my_array)

# Add an item to an array from a list using fromlist()
lst = [29,30,31,32,45]
my_array.fromlist(lst)
print(my_array)

# Remove any element using the Remove()
my_array.remove(90)
print(my_array)

# Remove the last element using the pop() method
my_array.pop()
print(my_array)

# Reverse an array using the reverse method
my_array.reverse()
print(my_array)

# Get a buffer info about an array using the buffer_info method
print(my_array.buffer_info())

# Check number of occurence of an element in an array
count = my_array.count(3)
print(count)

# Convert an array to a string using the string method
''''my_char_array = array('c', ['g','e','e','k'])
print(my_char_array.tostring())'''

# Convert an array to a list using tolist method
c = my_array.tolist()
print(c)
 