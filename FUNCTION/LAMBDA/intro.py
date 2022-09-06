"""
The lambda keyword creates an inline function that contains a single expression.
The value of this expression is
what the function returns when invoked.
"""
example = lambda : "hello"
print(example())
print()

s = lambda x : x * x
print(s(2))

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