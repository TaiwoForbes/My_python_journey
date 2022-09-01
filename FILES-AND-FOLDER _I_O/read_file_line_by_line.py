with open("taiwo.txt", "r") as f:
    line = []
    for lines in f:
        line.append(lines.strip("\n"))
print(line)

# This consider bad practice though , using an iterator  and readline() together
with open('taiwo.txt','r') as f:
    while True:
        current_line = f.readline()
        if current_line == '':
            #We have reach the end of  the line
            break
        print(current_line)

with open("taiwo.txt") as f:
    read = f.read()
    print(read)

