num = int(input("Ener your number:"))

for i in range(num+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()

print()

for i in range(num+1):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()


print()

for i in range(num+1):
    for j in range(i):
        print(i,end = " ")
    print()

print()

for i in range(num):                     
    for j in range(i+1):
        print(num-i,end = " ")
    print()

print()

for i in range(num):
    for j in range(i + 1):
        print(num-j,end = " ")
    print()

print()

for i in range(num):
    for j in range(i+1 ,0,-1):
        print(num-j+1,end = " ")
    print()


print()

for i in range(num):
    for j in range(num,i,-1):
        print(" ",end = " ")
    for j in range(i+1 ,0,-1):
        print(num-j+1,end = " ")
    print()

