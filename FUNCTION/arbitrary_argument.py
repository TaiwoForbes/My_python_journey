# Arbitrary number of positional arguments:

def func(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(func(1,2,3,4,5,6,7,8,9,10))

# Arbitrary number of keyword arguments
def func2(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
print(func2(value1 = 20, value2 = 30, value3 = 40))
dict = {"names" : {"taiwo", "shola", "tunde"}, "age" : [19,20,21,22,23]}
print(func2(**dict))