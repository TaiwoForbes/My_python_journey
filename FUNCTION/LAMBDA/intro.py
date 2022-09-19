"""
Lambda works almost the same way a "def" works
The lambda keyword creates an inline function that contains a single expression.
The value of this expression is
what the function returns when invoked.
"""
from tkinter import Y


example = lambda : "hello"
print(example())
print()

s = lambda x : x * x
print(s(2))
print()

sum = lambda x,y : x + y 
print(sum(2,3))
print()

# Using lambda as a ternary
can_vote = lambda age : True if age >= 18 else False
print(can_vote(1))
print()


# Using lambda as a dictionary
attack = {"quick": (lambda : print("Quick Attack")),
        "power": (lambda : print("Power Attack")),
        "missed": (lambda : print("Quick Attack"))}


import random
attack_keys = random.choice(list(attack.keys())) # random.choice works on a list. Hence we need to convert our keys into a list.
attack[attack_keys]() # Since our lambda function is returning a dict, we need it to behave like a dict itself.
print()


# lambdas can take arguments, too.
strip_and_upper_case = lambda s : s.strip().upper()
print(strip_and_upper_case("   hello    "))

# They can also take arbitrary number of arguments / keyword arguments, like normal functions.
greeting = lambda x, *args, **kwargs : print(x,args,kwargs)
greet = greeting("hello", "taiwo", welcome = "Nice meeting you")
print(greet)

# lambdas are commonly used for short functions that are convenient to define at the point where they are called
#(typically with sorted, filter and map).

list = [" foo ", " bAR", "BaZ "]
# This will ignore the white spaces and the upper
sort = sorted((list),key = lambda x : x.strip().upper())
print(sort)

# sorted ignoring only the white space
sort = sorted((list), key = lambda x : x.strip())
print(sort)
print()

# Example with map function
sort_with_map = sorted(map(lambda x : x.strip().upper(), list))
print(sort_with_map)

# One can call other functions (with/without arguments) from inside a lambda function
def foo(msg):
    return (msg)

greetings = lambda x = "hello world": foo(x)
print(greetings())

f = lambda x : x*2
print(f(2))