# The heapq function is used to find the largest or smallest value in a list
# This module takes two arguement,one for the number sepcified and the second is the collection itself
import heapq
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
# This print the largest in  a collection
print(heapq.nlargest(1,numbers))

# This prints the smallest in a collecton
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nsmallest(1,numbers))


people = [
 {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
 {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
 {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
 {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
 {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
 {'firstname': 'John', 'lastname': 'Roe', 'age': 45}
]
oldest = heapq.nlargest(2,people, key = lambda x : x['age'])
print(oldest)
print()
print()

youngest = heapq.nsmallest(1,people,key = lambda x : x["age"])
print(youngest)
print()
print()

numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]
heapq.heapify(numbers)
print(numbers)
print()
print()

heapq.heappop(numbers) 
print(numbers)
print()
print()
heapq.heappop(numbers)
print(numbers)
