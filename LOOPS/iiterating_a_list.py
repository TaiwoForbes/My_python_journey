lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

for word in lst:
    print(word[:1], end="") # Print the first letter
print()

print("--------------")

message = "Random Access Memory".split()

for words in message:
    print(words[:1])

print("--------------")
print("--------------")


for idx,s in enumerate(lst):
    print("{} has index of {}".format(s,idx))

print("--------------")