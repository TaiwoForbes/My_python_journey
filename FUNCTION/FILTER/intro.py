# Filter takes a function and a collection. It returns a collection of every item for which the function returned True.
arr = [1,2,3,4,5]
sample = [i for i in filter(lambda x : x % 2  == 0,arr)]
print(sample)
print()
print()
print()

# -----PROBLEM-----
# Find the multiple of 9 from a random 100 value list with values between 1,1000
import random
random_list = list(random.randint(1,1001) for i in range(1,100)) # This get a value between 1-1000 in range of 100

result = [i for i in filter(lambda x : x % 9 == 0, random_list)]
print(result)
print(list(filter(lambda x : x % 9 == 0, random_list))) # This code wors exactly the same as the above.
