data = [
        [1, 2], 
        [3, 4], 
        [5, 6]]
output = []

for row in data:
    for column in row:
        output.append(column)
print(output) 
print()
print()

# The above code is equivalent to the code below
result = [column for row in data for column in row]
print(result)
print()
print()


data = [[1], [2, 3], [4, 5]]
lst = []
for row in data:
    for column in row:
        if len(row) <= 2 and  column != 5:
            lst.append(column)
print(lst)
print()
print()

# Summation of 2D matrix
sum = [x + y for x in [1,2,3] for y in [5,6,7]]
print(sum)
print()
print()

sum2 = [[x + y for x in [1,2,3]] for y in [5,6,7]]
print(sum2)
print()
print()


matrix = [
            [1,2,3],          
            [4,5,6],          
            [7,8,9]
         ]
l = [[row[i] for row in matrix] for i in range(len(matrix))]
print(l)
print()

#  Iterate two or more list simultaneously within list comprehension 
list_1 = [1, 2, 3 , 4]  
list_2 = ['a', 'b', 'c', 'd'] 
list_3 = ['6', '7', '8', '9']

iteration = [(x,y,z) for x,y,z in zip(list_1,list_2,list_3)]
print(iteration)