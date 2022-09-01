"""
In Python, the itertools.groupby() method allows developers to group values of an iterable class based on a
specified property into another iterable set of values.
"""
from itertools import groupby


things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"), \
 ("vehicle", "speed boat"), ("vehicle", "school bus")]

dic = {}
f = lambda x : x[0]
for key,group in groupby(sorted(things,key=f),f):
    dic[key] = list(group)
print(dic)
print()
print()

# This example illustrates how the default key is chosen if we do not specify any
c = groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])
dics = {}

for k,v in c:
    dics[k] = list(v)
print(dics)
print()
print()

# Unsorted version
list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), \
 'wombat', 'mongoose', 'malloo', 'camel']
c = groupby(list_things, key = lambda x : x[0])
dict = {}
for k,v in c:
    dict[k] = list(v)
print(dict)
print()
print()

# Sorted Version
list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat', ('persons', 'man', 'woman'), \
 'wombat', 'mongoose', 'malloo', 'camel']
sorted_list = sorted(list_things,key = lambda x : x[0])
print(sorted_list)
print()
c = groupby(sorted_list, key = lambda x : x[0])
dict = {}
for k,v in c:
    dict[k] = list(v)
print(dict)
print()
print()
