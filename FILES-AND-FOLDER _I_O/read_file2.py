with open('taiwo.txt', 'r') as fileobj:
 # this method reads line by line:
    lines = []
    for line in fileobj:
        lines.append(line.strip())
print(lines)
