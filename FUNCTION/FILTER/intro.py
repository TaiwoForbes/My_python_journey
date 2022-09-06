# Reduce takes a function and a collection of items. It returns a value that is created by combining the items.
arr = [1,2,3,4,5]
sample = [i for i in filter(lambda x : x > 3,arr)]
print(sample)
