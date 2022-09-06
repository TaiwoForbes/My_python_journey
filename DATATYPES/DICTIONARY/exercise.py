# Getting a value in a dictionary
first_dict = {"Apple" : 10, "banana" : 5, 'orangr' : 4, "Guava" : 60}
print(first_dict.keys())
print()
# Getting a key in a dictionary
print(first_dict.values())
print()
# Getting both key and values in a dictionary
print(first_dict.items())
print()
# Remove sn item using pop()
first_dict.pop("Apple")
print(first_dict)
# Popitem method will remove the last item
first_dict.popitem()
print(first_dict)
print()

# Using loop
for k,v in first_dict.items():
    print(k,v)
print()
print()

# DICTIONARY COMPREHENSION
first_list = ["math", "eng", "phy", "chm"]
second_list = [90,100,50,60]
dict_sub = {key:value for key,value in zip(first_list, second_list) }
print(dict_sub)
print()

# Sinlge condition
dict = {"math": 21, "eng" : 51, "phy" : 30 ,"chm" : 8}
dict_output = {key:value for key,value in dict.items() if value % 2 == 0}
print(dict_output)
# multiple condition
dict = {"math": 21, "eng" : 51, "phy" : 30 ,"chm": 8}
dict_output = {key:value for key,value in dict.items() if value > 10 if value % 2 == 0}
print(dict_output)


# CHANGING NAME OF DICTIONARY KEY
animal_dict = {
    "Name" : "Dog",
    "age"  : 5,
    "weight" : 4,
    "Country" : "US",
    "city" : "Califonia"
}
print(animal_dict)
animal_dict["name"] = animal_dict.pop("Name")
print(animal_dict)
print()
print()

# Getting a min and max in a dictionary

# so i will referencing dict_value here, i dont want to type
print(min(dict_sub, key = dict_sub.get))
print(max(dict_sub, key = dict_sub.get))
print()
# Gettiing the sum of the value
print(sum(dict_sub.values()))
# Getting the multiplications of a dict
multiple  = 1
for i in dict_sub:
    multiple = multiple * dict_sub[i]
print(multiple) # 90 * 100 * 50 * 60 = 27000000