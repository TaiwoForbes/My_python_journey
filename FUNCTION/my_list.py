"""The lambda keyword creates an inline function that contains a single expression
"""
def greeting():
    return "Hello"
print(greeting())

# The above function can also be written as this below
greetme = lambda : "hello"
print(greetme)

strip_and_uppercase = lambda x : x.strip().upper()
print(strip_and_uppercase("  hello  "))

def give():
    return 
print(give())