str = "Hello"
print(str)
print("--------->")
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[0:4])
print(str[-1])

print("------->")


i = 0
while i < len(str):
    print(str[i], end='')
    i = i + 1
print()

strings = "Welcome to first Bank"
# Circle through in pairs
for i in range(0, len(strings) - 1):
    print(strings[i] + strings[i+1])
