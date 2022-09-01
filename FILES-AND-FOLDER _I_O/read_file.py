# This read a file, it makes a list
with open("taiwo.txt", "r") as fileobj:
    lines = fileobj.readlines()
print(lines)