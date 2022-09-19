"""Map takes a function and a collection of items. It makes a new, empty collection,
   runs the function on each item in
   the original collection and inserts each return value into the new collection. 
   It returns the new collection.
"""

One2ten = range(1,10)
double_num = lambda x : x * 2
print(list(map(double_num,One2ten)))
print()
print()

list1 = [1,2,3,4,6]
list2 = [4,6,8,9,2]
print(list(map(lambda x,y : x + y, list1,list2)))
print()
print()


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





