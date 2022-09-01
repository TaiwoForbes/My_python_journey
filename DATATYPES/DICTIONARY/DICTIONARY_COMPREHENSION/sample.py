dict = {x: x * x  for x in [1,2,3,4,5]}
print(dict)

names = {name: len(name) for name in ["stack", "overflow","course_rep"] if len(name) > 6}
print(names)

#Starting with a dictionary and using dictionary comprehension as a key-value pair ﬁlter
initial_dict = {'x': 1, 'y': 2}
x = {key:value for key,value in initial_dict.items() if key == "x"}
print(x)

# Switching key and value of dictionary (invert dictionary)
swapped = {key:value for value,key in initial_dict.items()}
print(swapped)

# Merging Dictionaries
dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}
merge = {key:value for d in [dict1,dict2] for key,value in d.items() }
print(merge)

merged = {**dict1,**dict2}
print(merged)