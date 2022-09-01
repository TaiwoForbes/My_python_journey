dict = {"color": "red", "age": 19}

# Adding a new key with value to a dictionary
dict["sex"] = "male"
print(dict)
print()
# Adding a list to a dictionary
dict["lst"] = [1,2,3,4]
print(dict)
print()
# Adding a dictionary to a dictionay
dict['new_dict'] = {'nested_dict': 1}
print(dict)
print()
# Deleting a key from a dictionary
del dict["lst"]
print(dict)
print()
# Set a default key but it doesnt add key to the exiting dict
dict.get("Foo", 'Bar')
print(dict)
print()
# This add to the exiting dict
dict.setdefault("Foo", 'Bar')
print(dict)
print()

from collections import defaultdict
d = defaultdict(int)
d["keys"]
d["keys"] = 5
d["keys"]
print(d)
print()

# Accessing keys
print(dict.keys())


# Accessing Values
print(dict.values())


# Accessing keys and Values
print(dict.items())

# Since we are trying to access a value that doesnt exit, it would return None
x = dict.get("trans")
print(x)
# We should get a default value of yes here but not in the intitial dict
x = dict.get("trans", "yes")
print(x)

print(dict)


