set = {x for x in range(10)}
print(set)

# A set of  even numbers
setOfEven = {x for x in range(10) if x % 2 == 0}
print(setOfEven)

# Unique alphabetic character of a string
text =  "When in the Course of human events it becomes necessary for one people..."
unique = {ch.lower() for ch in text if ch.upper()}
print(unique)