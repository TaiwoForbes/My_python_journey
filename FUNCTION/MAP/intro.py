"""Map takes a function and a collection of items. It makes a new, empty collection,
   runs the function on each item in
   the original collection and inserts each return value into the new collection. 
   It returns the new collection.
"""
list = ["Ayo", "mary", "tunde"]
name = map(len, list)
print(name)

