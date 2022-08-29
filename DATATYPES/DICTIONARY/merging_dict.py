fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fish_dog = {**fish,**dog}
print(fish_dog)


from collections import ChainMap

fish_dog = dict(ChainMap(dog,fish))
print(fish_dog)

print()
print()
print()


import itertools
options = {    
            "x": ["a", "b"],    
            "y": [10, 20, 30]
          }
keys = options.keys()
values =(options[key] for key in keys)
combinations = [dict(zip(keys,combinations)) for combinations in itertools.product(*values)]
print(combinations)