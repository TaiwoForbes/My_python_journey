"""Map takes a function and a collection of items. It makes a new, empty collection,
   runs the function on each item in
   the original collection and inserts each return value into the new collection. 
   It returns the new collection.
"""
lst = ["Ayo", "mary", "tunde"]
name = list(map(len, lst))
print(name)
print()

# Series of parallel mapping
insects = ['fly', 'ant', 'beetle', 'cankerworm']
mapping = list(map(lambda x: x + " is an insect", insects))
for item in mapping:
   print(item)
print(list(map(len, insects)))





